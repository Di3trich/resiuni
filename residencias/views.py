from django.shortcuts import render
from django.http import HttpResponse
from models import *

def show_main(request):
    #sede = Sede.objects.all()


    return HttpResponse("Esta es la pagina principal")


# Create your views here.
