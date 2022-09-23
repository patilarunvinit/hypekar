from django.urls import path
from . import views

urlpatterns=[
    path('reg/',views.reg),
    path('login/',views.slogin),
    path('logout/',views.slogout),
    #path('auth_login/',views.auth_login),
    path('contact/',views.contactForm),
    path('carbrand/',views.carbrand),
    path('carmodel',views.carmodel),
    path('carform/',views.CarForm),
    path('test/',views.test),

]