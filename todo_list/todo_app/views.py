from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello How are you")

def create(request):
    return HttpResponse("Create Todo")