from django.forms import ModelForm
from schemas_structure.models import DataSet


class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        fields = ['rows']