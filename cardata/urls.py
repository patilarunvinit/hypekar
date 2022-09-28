from django.urls import path
from . import views

urlpatterns=[
    path('allcars/', views.allcars),
    path('carbrand/', views.carbrand),
    path('carmodel', views.carmodel),

]