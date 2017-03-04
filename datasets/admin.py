from django.contrib import admin

from .models import Dataset


class DatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_file')
    search_fields = ('name', 'description', 'tags')


admin.site.register(Dataset, DatasetAdmin)
