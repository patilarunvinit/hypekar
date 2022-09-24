from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import carsserializer, cars2serializer, cars3serializer
from .models import cars



# Create your views here.


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
