from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


testString = """
<h1>Hello World!</h1>
"""

def index(request):
    #Django invia la richiesta e viene restituita un risposta in HTML
    return HttpResponse(testString)

