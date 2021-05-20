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
    aframe_thing = """<!DOCTYPE html>
<html>
  <head>
    <title><b>Hello, from Bill! - A-Frame</title>
    <meta name="description" content="Hello, WebVR! - A-Frame">
    <script src="https://aframe.io/releases/0.5.0/aframe.min.js"></script>
  </head>
  <body>
    <a-scene>
      <a-box position="-1 3 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
      <a-sphere position="0 1.25 -8" radius="1.25" color="#EF2D5E" scale="10 10 10">
        <a-ring position="-1 1 0" color="#B96FD3"></a-ring>
        <a-ring position="1 1 0" color="#B96FD3"></a-ring>
      </a-sphere>
      <a-cylinder position="-1.5 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
      <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
      <a-sky color="#ECECEC"></a-sky>
    </a-scene>
  </body>
</html>"""
    return HttpResponse(aframe_thing)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
