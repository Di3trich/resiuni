from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from models import Sede, Institucion, Residencia, Tipo_residencia

import json

def super_function(request):
    residencias_filters = Residencia.objects.values()
        #copeo los datos

    if 'tipo_residencia' in request.GET:
        #VERIFICAR QUE PRICE_FROM<=PRICE_UNTIL
        if request.GET['price_from'] > request.GET['price_until']:
            return HttpResponse("ERRRRRORRRRR")

        input_data = {}
        #input_data['tipo_residencia'] = ['Habitacion','Departamento','Casa']
        input_data['tipo_residencia'] = request.GET.getlist('tipo_residencia')

        input_data['genero'] = request.GET['genero']
        input_data['price_from'] = request.GET['price_from']
        input_data['price_until'] = request.GET['price_until']

        residencias = Residencia.objects.values().filter(tipo_residencia__name = input_data['tipo_residencia']).filter(gender = input_data['genero'] )
        residencias_filters = []
        for residencia in residencias:
            if not (residencia['price_until']<input_data['price_from'] or input_data['price_until'] < residencia['price_from']):
                residencias_filters.append(residencia)

        return render(request, 'form2.html', residencias_filters)

    c = Context()
    c['residencias_filters'] = residencias_filters
    return render(request, 'form1.html', residencias_filters)
    #return HttpResponse(json.dumps(residencias_filters), content_type="application/json")



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
    #residencias = Residencia.objects.order_by('latitude').order_by('longitude')

    residencias = Residencia.objects.all()

    datas = []
    for residencia in residencias:
        data = {}
        data['id_residencia'] = residencia.id
        data['latitude_residencia'] = residencia.latitude
        data['longitude_residencia'] = residencia.longitude
        data['color_residencia'] =residencia.tipo_residencia.color
        datas.append(data)

    return HttpResponse(json.dumps(datas), content_type="application/json")

def show_residencias_in_nav(request):

    residencias = Residencia.objects.order_by('latitude').order_by('longitude')
    datas = []
    for residencia in residencias:
        data = {}
        data['id_residencia'] = residencia.id
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
