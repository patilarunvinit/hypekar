from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import cars

# Register your models here.
class carsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("brand","model_name","basic","standard","premium")
admin.site.register(cars, carsAdmin)