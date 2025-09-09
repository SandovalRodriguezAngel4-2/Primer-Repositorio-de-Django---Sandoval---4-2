from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def saludo(request):
    return HttpResponse("Hola Soy Sandoval Rodriguez desde Django, listo para PythonAnywhere!")
