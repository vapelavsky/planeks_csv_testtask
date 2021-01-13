from django.urls import path
from . import views

urlpatterns = [
    path('create_schema/', views.SchemaCreateView.as_view(), name='SchemaCreateView'),
    path('update_schema/<int:pk>/', views.SchemaUpdateView.as_view(), name='SchemaUpdateView'),
    path('delete_schema/<int:pk>/', views.SchemaDeleteView.as_view(), name='SchemaDeleteView'),
    path('generate_data/<int:pk>/', views.DataSetView.as_view(), name='DataSetView'),
    path('', views.SchemaListView.as_view(), name='SchemaListView'),
]
