# Generated by Django 3.1.4 on 2021-01-11 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('column_separator', models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)')], max_length=2)),
                ('string_character', models.CharField(choices=[('"', 'Double-quote (")'), ("'", "Single-quote (')")], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('rows', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('Ready', 'Ready'), ('Processing', 'Processing')], max_length=15)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemas_structure.schema')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('range_from', models.IntegerField(blank=True, null=True)),
                ('range_to', models.IntegerField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(null=True)),
                ('column_type', models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job'), ('Email', 'Email'), ('Domain name', 'Domain name'), ('Phone number', 'Phone number'), ('Company name', 'Company name'), ('Text', 'Text'), ('Integer', 'Integer'), ('Address', 'Address'), ('Date', 'Date')], max_length=12)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemas_structure.schema')),
            ],
        ),
    ]
