from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializers import contanctserializer, carsserializer, cars2serializer, cars3serializer, mycarserializer
from .models import contanctpage, cars, mycar

from rest_framework.response import Response


from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)



# Create your views here.
# This view is for getting subscriber data and posting subscriber data
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





# this view is for subscriber Login
@csrf_exempt
def auth_login(request):
    if request.method == 'POST':
        data2=JSONParser().parse(request)
        username=data2["username"]
        password=data2["password"]

        try:
            a = authenticate(username=username, password=password)
            print(a)
            if a is not None:

                return JsonResponse({"status": "1", "massage":"logged in successfuly"}, safe=False)

            else:
                return JsonResponse({"status": "0", "massage": "email or password wrong"}, safe=False)

        except:
            return JsonResponse({"status": "0", "massage": "email or password wrong"}, safe=False)





@csrf_exempt
@permission_classes((AllowAny,))
def slogin(request):
   if request.method == "POST":
       data2 = JSONParser().parse(request)
       username = data2["username"]
       password = data2["password"]
       print(username,password)
       if username=="" or password =="":
           return JsonResponse({'error': 'Please provide both username and password'},
                           status=HTTP_400_BAD_REQUEST)
       user = authenticate(username=username, password=password)
       if not user:
           return JsonResponse({'error': 'Invalid Credentials'},
                           status=HTTP_404_NOT_FOUND)
       else:
           login(request,user)
           request.session['email'] = user.email
           token, _ = Token.objects.get_or_create(user=user)
           return JsonResponse({'token': token.key,'first_name':user.first_name,'last_name':user.last_name,'username':user.username}, status=HTTP_200_OK)



@csrf_exempt
def slogout(request):
    if request.method =='GET':
        try:
            del request.session['email']
        except KeyError:
            pass
        return JsonResponse({"massage": "logout successfuly"}, safe=False)




@csrf_exempt
def contactForm(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = contanctserializer(data=data1)

        if outdata.is_valid():
            outdata.save()
            return JsonResponse(outdata.data, safe=False)
        else:
            return JsonResponse(outdata.errors, safe=False)

    elif request.method =='GET':
        a=contanctpage.objects.all()
        b=contanctserializer(a, many=True)
        return JsonResponse(b.data, safe=False)



@csrf_exempt
def carbrand(request):
    if request.method =='GET':
        output = cars.objects.order_by().values('brand').distinct()
        outdata = cars2serializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)



@csrf_exempt
def carmodel(request):
    if request.method =='GET':
        brand = request.GET['brand']
        output = cars.objects.all().filter(brand=brand).values('model_name')
        outdata = cars3serializer(output, many=True)
        return JsonResponse(outdata.data, safe=False)



@csrf_exempt
def CarForm(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = mycarserializer(data=data1)
        if outdata.is_valid():
            outdata.save()
            return JsonResponse(outdata.data, safe=False)
        else:
            return JsonResponse(outdata.error, safe=False)

    elif request.method == "GET":
        m = mycar.objects.all()
        n = mycarserializer(m, many=True)
        return JsonResponse(n.data, safe=False)



@csrf_exempt
def mycardata(request):
    if request.method =='GET':
        email = request.session.get('email')
        data=mycar.objects.filter(email=email)
        output=mycarserializer(data, many=True)
        try:
            data[0]
            return JsonResponse(output.data, safe=False)

        except:

            return JsonResponse({"massage": "login 1st"}, safe=False)
