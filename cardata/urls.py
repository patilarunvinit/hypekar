from django.urls import path
from . import views

urlpatterns=[
    path('carbrand/', views.carbrand),
    path('carmodel', views.carmodel),

]