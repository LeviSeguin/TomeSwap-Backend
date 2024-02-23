from django.shortcuts import render, HttpResponse
from django.http import JsonResponse #for API requests

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def test_api(request):
    return "this is the test api content"

