from django.contrib import admin

from apps.converter.models import Converter


@admin.register(Converter)
class ConverterAdmin(admin.ModelAdmin):
    list_display = ('from_currency', 'to_currency',)
    list_display_links = ['from_currency']
