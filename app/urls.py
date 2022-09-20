from django.urls import path
from . import views

urlpatterns=[
    path('reg/',views.reg),
    path('login/',views.slogin),
    #path('auth_login/',views.auth_login),
    path('contact/',views.contactForm),

]