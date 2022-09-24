
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import mycarserializer
from .models import mycar


# Create your views here.

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