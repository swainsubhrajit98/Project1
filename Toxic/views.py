from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Swapnajit(request):
    return HttpResponse('<h1>Subhrajit You are selected for next round</h1>')

def Tapu(request):
    return HttpResponse('<h1><marquee>Swapnajit<br> is my Younger Brother.</marquee></h1>')

def App(requst):
    return HttpResponse('<h1><marquee>Udy is my Best Friend</marquee></h1>')