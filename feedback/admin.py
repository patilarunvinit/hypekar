from django.contrib import admin
from .models import FeedBack
# Register your models here.
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ("email", "description","rating","location","name")
admin.site.register(FeedBack,FeedBackAdmin)