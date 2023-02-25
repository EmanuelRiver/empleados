from django.shortcuts import render
from django.http import HttpResponse
from carga_empleados.models import Empleado, empresa_terciarizada,vehiculo_empresarial
from carga_empleados.forms import EmpleadosFormularios,EmpresaFormularios,VehiculoFormularios
# Create your views here.


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

def empresa_terciarizada(request):
        if request.method == 'POST':
            miFormulario=EmpresaFormularios(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion=miFormulario.cleaned_data
                empleados = empresa_terciarizada(nombre=informacion["nombre"],razon_social=informacion['razon social'],cuit=informacion['cuit'])
                empleados.save()
                return render(request,'carga_empleados/inicio.html')
        else:
             miFormulario=EmpresaFormularios()
        return render(request,'carga_empleados/empresa_terciarizada.html',{'miFormulario':miFormulario})

def vehiculo_empresarial(request):
        if request.method == 'POST':
            miFormulario=VehiculoFormularios(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion=miFormulario.cleaned_data
                empleados = vehiculo_empresarial( marca=informacion["Marca"],modelo=informacion['Modelo'],patente=informacion['Dominio'])
                empleados.save()
                return render(request,'carga_empleados/inicio.html')
        else:
             miFormulario=VehiculoFormularios()
        return render(request,'carga_empleados/vehiculo_empresarial.html',{'miFormulario':miFormulario})
