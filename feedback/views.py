from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import FeedBackserializer
from .models import FeedBack



# Create your views here.


@csrf_exempt
def feedbackform(request):
    if request.method =='POST':
        data1 = JSONParser().parse(request)
        outdata = FeedBackserializer(data=data1)

        if outdata.is_valid():
            outdata.save()
            return JsonResponse(outdata.data, safe=False)
        else:
            return JsonResponse(outdata.errors, safe=False)

    elif request.method == 'GET':
        data = FeedBack.objects.all()[:6]
        output = FeedBackserializer(data, many=True)
        return JsonResponse(output.data, safe=False)

