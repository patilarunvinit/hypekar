from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
def reg(request):
    if request.method =='POST':
        try:
            data = JSONParser().parse(request)
            username = data['username']
            password = data['password']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            print(username, password)
            out = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                           last_name=last_name)
            out.save()
            return JsonResponse({"massage": "Registration successful"}, safe=False)

        except:
            return JsonResponse({"massage": "username already exists"}, safe=False)
