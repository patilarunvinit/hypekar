from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import bookingserializer
from .models import booking


# Create your views here.

@csrf_exempt
def book(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = bookingserializer(data=data1)
        print(outdata)
        if outdata.is_valid():
            outdata.save()
            return JsonResponse(outdata.data, safe=False)
        else:
            return JsonResponse(outdata.error, safe=False)

    elif request.method == "GET":
        m = booking.objects.all()
        n = bookingserializer(m, many=True)
        return JsonResponse(n.data, safe=False)
