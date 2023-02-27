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
                empresa = empresa_terciarizada(nombre=informacion["nombre"],razon_social=informacion['razon social'],cuit=informacion['cuit'])
                empresa.save()
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
                vehiculo = vehiculo_empresarial( marca=informacion["Marca"],modelo=informacion['Modelo'],patente=informacion['Dominio'])
                vehiculo.save()
                return render(request,'carga_empleados/inicio.html')
        else:
             miFormulario=VehiculoFormularios()
        return render(request,'carga_empleados/vehiculo_empresarial.html',{'miFormulario':miFormulario})

def leerempleados(request):
     empleados = Empleado.objects.all()
     contexto = {'empleados':empleados}
     return render(request,'carga_empleados/leerEmpleados.html', contexto)

def eliminarEmpleado(request,nombre_empleado):
     empleado = Empleado.objects.get(nombre=nombre_empleado)
     empleado.delete()

     empleados = Empleado.objects.all()
     contexto = {'empleados': empleados}
     return render(request,"carga_empleados/leerEmpleados.html",contexto)

def editarEmpleado(request,nombre_empleado):
    empleado = Empleado.objects.get(nombre=nombre_empleado)
    if request.method == 'POST':
        miFormulario = EmpleadosFormularios(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empleado.nombre = informacion['nombre']
            empleado.apellido = informacion['apellido']
            empleado.cargo = informacion['cargo']

            empleado.save()

            return render(request,'carga_empleados/inicio.html')
    else:
        miFormulario = EmpleadosFormularios(initial={'nombre':empleado.nombre,'apellido':empleado.apellido,'cargo':empleado.cargo})
    return render(request,'carga_empleados/editarEmpleado.html',{'miFormulario':miFormulario,'empleado_nombre':empleado.nombre})
