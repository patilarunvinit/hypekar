from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from mycar.serializers import mycarserializer ,mycarbrandserializer,mycarmodelserializer
from mycar.models import mycar



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
           return JsonResponse({'token': token.key,"massage":"logged in successfuly",'first_name':user.first_name,'last_name':user.last_name,'username':user.username,'email':user.email}, status=HTTP_200_OK)



@csrf_exempt
def slogout(request):
    if request.method =='GET':
        logout(request)
        try:
            del request.session['email']
        except KeyError:
            pass
        return JsonResponse({"massage": "logout successfuly"}, safe=False)



@csrf_exempt
def mycardata(request):
    if request.method =='GET':
        email = request.GET['email']
        data=mycar.objects.filter(email=email)
        output=mycarserializer(data, many=True)
        try:
            data[0]
            return JsonResponse(output.data, safe=False)

        except:

            return JsonResponse({"massage": "login 1st"}, safe=False)





@csrf_exempt
def mycarbrand(request):
    if request.method =='GET':
        email = request.GET['email']
        data=mycar.objects.filter(email=email).values("brand").distinct()
        output=mycarbrandserializer(data, many=True)
        try:
            data[0]
            return JsonResponse(output.data, safe=False)

        except:

            return JsonResponse({"massage": "login 1st"}, safe=False)




@csrf_exempt
def mycarmodel(request):
    if request.method =='GET':
        brand = request.GET['brand']
        email = request.GET['email']
        data=mycar.objects.filter(email=email,brand=brand).values("model_Name")
        output=mycarmodelserializer(data, many=True)
        try:
            data[0]
            return JsonResponse(output.data, safe=False)

        except:

            return JsonResponse({"massage": "login 1st"}, safe=False)



