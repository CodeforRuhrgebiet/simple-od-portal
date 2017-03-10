from django.contrib import admin

from .models import Dataset


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    """
    we make this model readonly in admin,
    because the "source of truth" is the github repo!
    """
    date_hierarchy = 'created_ts'
    list_display = ('name',)
    search_fields = ('name', 'description', 'tags', 'file_content')
    list_filter = ('published_date', 'created_ts')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [f.name for f in obj._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
