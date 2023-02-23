from django.shortcuts import render
from django.http import HttpResponse
from carga_empleados.models import Empleado, empresa_terciarizada,vehiculo_empresarial
from carga_empleados.forms import EmpleadosFormularios
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
        if request.method == 'POST':
            miFormulario= EmpleadosFormularios(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion=miFormulario.cleaned_data
                empleados = Empleado(nombre=informacion["nombre"],apellido=informacion['apellido'],cargo=informacion['cargo'])
                empleados.save()
                return render(request,'carga_empleados/inicio.html')
        else:
            miFormulario=EmpleadosFormularios()
    
        return render(request,"carga_empleados/empleados.html",{'miFormulario':miFormulario})
    #return render(request, "carga_empleados/empleados.html")
    #return HttpResponse("Vista empleados cargados al sistema")

def empresa_terciarizada(request):
    return render(request, "carga_empleados/empresa_terciarizada.html")

def vehiculo_empresarial(request):
    return render(request,"carga_empleados/vehiculo_empresarial.html")
"""
def empleadosFormularios(request):
    if request.method == 'POST':
        empleados = Empleado(request.POST["nombre"],(request.POST['apellido'],(request.POST['cargo'])))
        empleados.save()
        return render(render,'carga_empleados/inicio.html')
    return render(request,"carga_empleados/empleadosFormularios.html")

"""
"""
def empleadosFormularios(request):
    if request.method == 'POST':
        miFormulario= EmpleadosFormularios(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            empleados = Empleado(nombre=informacion["nombre"],apellido=informacion['apellido'],cargo=informacion['cargo'])
            empleados.save()
            return render(request,'carga_empleados/inicio.html')
    else:
        miFormulario=EmpleadosFormularios()
    
    return render(request,"carga_empleados/empleados/empleadosFormularios.html",{'miFormulario':miFormulario})
"""