from django.contrib import admin

from derby.names.models import Name


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
