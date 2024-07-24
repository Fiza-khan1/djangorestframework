from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializer import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer

def student_detail(request):
    student=Student.objects.get(id=1)
    serializer=StudentSerializer(student)
    print('PYTHON DATA',serializer)
    # jsonData=JSONRenderer().render(serializer.data)
    # print(jsonData)
    # return HttpResponse(jsonData,content_type='application/json')
    return JsonResponse(serializer.data)


def student_detail_all(request):
    student=Student.objects.all()
    serializer=StudentSerializer(student,many=True)
    print('PYTHON DATA',serializer)
    # jsonData=JSONRenderer().render(serializer.data)
    # print(jsonData)
    # return HttpResponse(jsonData,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

    
    

