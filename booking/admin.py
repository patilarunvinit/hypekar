from django.contrib import admin
from .models import booking

# Register your models here.
class bookingAdmin(admin.ModelAdmin):
    list_display =("email", "customer_name", "customer_address", "service_address", "brand", "model", "service_type","time_slot","date")

admin.site.register(booking, bookingAdmin)