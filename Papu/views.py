from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Munna(request):
    return HttpResponse('<h1>Wecome Back to my Kingdom</h1>')
def Haneef(request):
    return HttpResponse('<h2>He is also my friend</h2>')
def Jsp(request):
    return HttpResponse('<marquee>Kishor is very rich</marquee>')