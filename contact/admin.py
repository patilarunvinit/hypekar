from django.contrib import admin
from .models import contanctpage
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display = ("firstName","lastName","type","mobileNumber")
admin.site.register(contanctpage, contactAdmin)