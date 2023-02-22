from django.shortcuts import render
from django.http import HttpResponse
from carga_empleados.models import Empleado
# Create your views here.

"""
def empleados (self):
    empleado = Empleado(nombre="Ricardo",apellido="Rivero",cargo="operario")
    empleado.save()
    documentoDeTexto = f"---> nombre: {empleado.nombre} Apellido: {empleado.apellido} Cargo: {empleado.cargo}"
    return HttpResponse(documentoDeTexto)
"""
def Inicio(request):
    return render(request,"carga_empleados/inicio.html")
    #return HttpResponse("Vista inicio")

def empleados(request):
    return render(request, "carga_empleados/empleados.html")
    #return HttpResponse("Vista empleados cargados al sistema")

