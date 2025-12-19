from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import user

# Create your views here.

# def demo(request):
#     return  render(request,"hello.html")

def insert(request):
    data = user(
        Name = "john",
        Age = 25,
        Phone = "1234567980",
        Place = "Kottakkal"
    )
    data.save()
    return HttpResponse("insertion success",data)

def displaydata(request):
    data = list(user.objects.values())
    return JsonResponse(data, safe=False)

def filterdata(request):
    data = user.objects.filter(Name="john").values()
    return JsonResponse(list(data), safe=False)