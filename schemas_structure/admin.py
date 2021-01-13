from django.contrib import admin
from schemas_structure.models import Schema, Column, DataSet

admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(DataSet)
