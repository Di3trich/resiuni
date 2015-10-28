from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from django.db.models import Q
from models import Sede, Institucion, Residencia, Tipo_residencia

import json

def super_function_show(request):
    residencias_filters = Residencia.objects.values()
    errors = []

    c = Context()
    if len(request.GET) > 0:

        if  request.GET['price_from'] > request.GET['price_until']:
            (request.GET['price_from'] , request.GET['price_until']) = ( request.GET['price_until'] , request.GET['price_from']  )
        if not ('tipo_residencia' in request.GET):
            errors.append("Seleccione un tipo de residencia")

        if not errors: # si no hay errores comienzo a realizar los filtros

            tipo_residencias = request.GET.getlist('tipo_residencia')
            query = Q()
            for tipo_residencia in tipo_residencias:
                query = query | Q(tipo_residencia__name = tipo_residencia)

            residencias = Residencia.objects.values().filter(query)

            if request.GET['genero'] == "Masculino y Femenino":
                tipo_genero =  ["Masculino y Femenino", "Femenino", "Masculino"]
                query = Q()
                for genero in tipo_genero:
                    query = query | Q(gender = genero)

                residencias = residencias.filter(query)
            else:
                residencias = residencias.filter(gender = request.GET['genero'])

            print len(residencias)

            #print 'comparar = ' + '[' + str(request.GET['price_from']) + ' : ' + str(request.GET['price_until']) + ']'
            residencias_filters = []
            #------------------------------- FILTRO POR PRECIOS ------------------------------------------------------
            for residencia in residencias:
                if (residencia['price_until'] < int(request.GET['price_from'])) or (int(request.GET['price_until']) < residencia['price_from']):
                    print '[' + str(residencia['price_from']) + ' : ' + str(residencia['price_until']) + ']'
                else:
                    residencias_filters.append(residencia)

            #----------------------------------FALTA LA FUNCION FILTRO POR AREA-------------------------------------------
            c['residencias_filters'] = residencias_filters
            return render(request, 'form2.html', c)

    c['residencias_filters'] = residencias_filters
    c['errors'] = errors
    return render(request, 'form1.html', c)
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
