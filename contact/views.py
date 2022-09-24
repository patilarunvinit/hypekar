
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import contanctserializer
from .models import contanctpage


# Create your views here.


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
