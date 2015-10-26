from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render
from models import Sede, Institucion

import json

def show_main(request):
    sede = Sede.objects.get(id = 1)
    c = Context()
    c['sede'] = sede
    #institucion = Institucion.objects.get(id = sede['institucion'])
    #c['institucion'] = institucionx
    return render(request, 'main.html' , c)

def another_main(request):
    sede = Sede.objects.get(id = 1)
    data={}
    data['latitude']=sede.latitude
    data['longitude']=sede.longitude
    data['id']=sede.id
    return HttpResponse(json.dumps(data), content_type="application/json")




# Create your views here.
