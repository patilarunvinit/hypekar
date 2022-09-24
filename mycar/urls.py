from django.urls import path
from . import views

urlpatterns=[
    path('carform/',views.CarForm),

]