from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from models import Sede, Institucion

def show_main(request):
    sede = Sede.objects.get(id = 1)
    c = Context()
    c['sede'] = sede
    #institucion = Institucion.objects.get(id = sede['institucion'])
    #c['institucion'] = institucionx
    return render(request, 'main.html' , c)


# Create your views here.
