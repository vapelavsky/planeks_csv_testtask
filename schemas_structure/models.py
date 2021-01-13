from django.db import models


class Schema(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    COMMA = ','
    SEMICOLON = ';'
    DOUBLEQUOTE = '"'
    SINGLEQUOTE = "'"

    COLUMN_SEPARATOR_CHOICES = [
        (COMMA, 'Comma (,)'),
        (SEMICOLON, 'Semicolon (;)')
    ]
    STRING_CHARACTER_CHOICES = [
        (DOUBLEQUOTE, 'Double-quote (")'),
        (SINGLEQUOTE, "Single-quote (')")
    ]
    column_separator = models.CharField(
        max_length=2,
        choices=COLUMN_SEPARATOR_CHOICES
    )

    string_character = models.CharField(
        max_length=2,
        choices=STRING_CHARACTER_CHOICES
    )


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    range_from = models.IntegerField(null=True, blank=True)
    range_to = models.IntegerField(null=True, blank=True)
    order = models.PositiveIntegerField(null=True)

    FULL_NAME = 'Full name'
    JOB = 'Job'
    EMAIL = 'Email'
    DOMAIN_NAME = 'Domain name'
    PHONE_NUMBER = 'Phone number'
    COMPANY_NAME = 'Company name'
    TEXT = 'Text'
    INTEGER = 'Integer'
    ADDRESS = 'Address'
    DATE = 'Date'

    COLUMN_TYPE_CHOICES = [
        (FULL_NAME, 'Full name'),
        (JOB, 'Job'),
        (EMAIL, 'Email'),
        (DOMAIN_NAME, 'Domain name'),
        (PHONE_NUMBER, 'Phone number'),
        (COMPANY_NAME, 'Company name'),
        (TEXT, 'Text'),
        (INTEGER, 'Integer'),
        (ADDRESS, 'Address'),
        (DATE, 'Date')
    ]
    column_type = models.CharField(
        max_length=12,
        choices=COLUMN_TYPE_CHOICES
    )


class DataSet(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    rows = models.IntegerField(null=True)

    class Status(models.TextChoices):
        READY = 'Ready'
        PROCESSING = "Processing"

    status = models.CharField(
        max_length=15,
        choices=Status.choices
    )
