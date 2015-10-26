from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from models import Sede, Institucion, Residencia

import json

def show_main(request):
    sede = Sede.objects.get(id = 1)
    institucion = Institucion.objects.get(id = int(sede.institucion.id))

    data = {}
    data['id_sede'] = sede.id
    data['name_institucion'] = institucion.name
    data['short_name_institucion'] = institucion.short_name
    data['name_sede'] = sede.name
    data['latitude_sede'] = sede.latitude
    data['longitude_sede'] = sede.longitude

    return HttpResponse(json.dumps(data), content_type="application/json")

def test(request):
    return render(request, 'index.html')


def show_residencias(request):
    residencias = Residencia.objects.order_by('latitude').order_by('longitude')
    datas = []
    for residencia in residencias:
        data = {}
        data['id_residencia'] = residencia.id
        data['latitude_residencia'] = residencia.latitude
        data['longitude_residencia'] = residencia.longitude
        data['color_residencia'] =residencia.tipo_residencia.color
        datas.append(data)

    return HttpResponse(json.dumps(datas), content_type="application/json")






def another_main(request):
    sede = Sede.objects.get(id = 1)
    data={}
    data['latitude']=sede.latitude
    data['longitude']=sede.longitude
    data['id']=sede.id
    return HttpResponse(json.dumps(data), content_type="application/json")




# Create your views here.
