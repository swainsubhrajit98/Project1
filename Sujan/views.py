from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ABC(request):
    return HttpResponse('<h3>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem vero amet ad eligendi numquam reiciendis, unde explicabo odit tempora eum delectus saepe voluptate eaque. Officia illo quo soluta vel voluptates eligendi dolorem veritatis facere.</h3>')
