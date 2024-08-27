from django.shortcuts import render
from django.http import HttpResponse
import datetime

def display(request):
    return HttpResponse('<h1>Hola mundo</h1>')

def displayDataTime(request):
    dt = datetime.datetime.now()
    s = '<b>Fecha y Hora actual: </b>'+str(dt)
    return HttpResponse(s)

def displayLogin(requestf):
    f = '<h1>Bienvenido</h1><br>'
    f+= '<label>Usuario:</label><br> <input></input><br>'
    f+= '<label>Contraseña:</label><br> <input></input><br>' 
    f+= '<button type="button">Ingresar</button>'
    return HttpResponse(f)