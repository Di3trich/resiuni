from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from models import Sede, Institucion, Residencia

def show_main(request):
    sede = Sede.objects.get(id = 1)
    c = Context()
    c['sede'] = sede
    institucion = Institucion.objects.get(id = int(sede.institucion.id))
    c['institucion'] = institucion

    data = {}
    data['name_institucion'] = institucion.name
    data['short_name_institucion'] = institucion.short_name
    data['name_sede'] = sede.name
    data['latitude_sede'] = sede.latitude
    data['longitude_sede'] = sede.longitude

    return HttpResponse()


def residencias(request):
    residencias = Residencia.objects.order_by('latitude').order_by('longitude')
    data = {}





# Create your views here.
