from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from schemas_structure.tasks import generate_data_task

from schemas_structure.models import Schema, Column, DataSet
from schemas_structure.forms import DataSetForm

column_formset = inlineformset_factory(
            Schema, Column, fields=('name', 'column_type', 'order', 'range_from', 'range_to'),
            labels={'name': 'Column name', 'column_type': 'Type',
                    'order': 'Order', 'range_from': 'From', 'range_to': 'To'},
            can_order=False, can_delete=True
        )


class SchemaListView(LoginRequiredMixin, ListView):
    model = Schema

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class SchemaCreateView(LoginRequiredMixin, CreateView):
    model = Schema
    fields = ['name', 'column_separator', 'string_character']
    success_url = reverse_lazy('SchemaListView')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["columns"] = column_formset(self.request.POST)
        else:
            data["columns"] = column_formset()
        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = self.get_context_data()
        columns = context["columns"]
        if not columns.is_valid():
            return super().form_invalid(form)
        self.object = form.save()
        columns.instance = self.object
        columns.save()
        return super().form_valid(form)


class SchemaUpdateView(LoginRequiredMixin, UpdateView):
    model = Schema
    fields = ['name', 'column_separator', 'string_character']
    success_url = reverse_lazy('SchemaListView')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["columns"] = column_formset(self.request.POST, instance=self.object)
        else:
            data["columns"] = column_formset(instance=self.object)
        return data

    def form_valid(self, form):
        form.instance.user = self.request.user
        context = self.get_context_data()
        columns = context["columns"]
        if not columns.is_valid():
            return super().form_invalid(form)
        self.object = form.save()
        columns.instance = self.object
        columns.save()
        return super().form_valid(form)


class SchemaDeleteView(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('SchemaListView')


class DataSetView(LoginRequiredMixin, FormMixin, ListView):
    model = DataSet
    form_class = DataSetForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(schema_id=self.schema_id)


    def form_valid(self, form):
        form.instance.schema_id = self.schema_id
        form.instance.status = DataSet.Status.PROCESSING

        dataset = form.save()

        generate_data_task.delay(dataset.id)

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        self.schema_id = kwargs["pk"]
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.path