from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import os
import requests

# Create your views here.
def v0_index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def v1_index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def v2_index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)


def index(request):
  
    return HttpResponse("index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
