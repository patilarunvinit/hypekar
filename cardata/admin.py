from django.contrib import admin
from .models import cars

# Register your models here.
class carsAdmin(admin.ModelAdmin):
    list_display = ("brand","model_name","basic","standard","premium")
admin.site.register(cars, carsAdmin)