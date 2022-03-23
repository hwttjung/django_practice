from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("씨포털입니다.")