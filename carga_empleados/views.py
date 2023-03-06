from django.shortcuts import render
from django.http import HttpResponse
from carga_empleados.models import Empleado, empresa_terciarizada,vehiculo_empresarial
from carga_empleados.forms import EmpleadosFormularios,EmpresaFormularios,VehiculoFormularios, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Inicio(request):
    return render(request,"carga_empleados/inicio.html")
    #return HttpResponse("Vista inicio")

def empleados(request):
        if request.method == 'POST':
            miFormulario= EmpleadosFormularios(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion=miFormulario.cleaned_data
                empleados = Empleado(nombre=informacion['nombre'],apellido=informacion['apellido'],cargo=informacion['cargo'])
                empleados.save()
                return render(request,'carga_empleados/inicio.html')
        else:
            miFormulario=EmpleadosFormularios()
    
        return render(request,"carga_empleados/empleados.html",{'miFormulario':miFormulario})

def Empresa_terciarizada(request):
        if request.method == 'POST':
            miFormulario=EmpresaFormularios(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion=miFormulario.cleaned_data
                empresa = empresa_terciarizada(nombre=informacion['nombre'],razon_social=informacion['razon_social'],cuit=informacion['cuit'])
                empresa.save()
                return render(request,'carga_empleados/inicio.html')
        else:
             miFormulario=EmpresaFormularios()
        return render(request,'carga_empleados/empresa_terciarizada.html',{'miFormulario':miFormulario})

def Vehiculo_empresarial(request):
        if request.method == 'POST':
            miFormulario=VehiculoFormularios(request.POST)
            print(miFormulario)

            if miFormulario.is_valid:
                informacion=miFormulario.cleaned_data
                vehiculo = vehiculo_empresarial(marca=informacion["marca"],modelo=informacion['modelo'],patente=informacion['patente'])
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
    return render(request,'carga_empleados/editarEmpleados.html',{'miFormulario':miFormulario,'nombre_empleado':nombre_empleado})

def leerEmpresas(request):
    empresa = empresa_terciarizada.objects.all()
    contexto = {'empresa':empresa}
    return render(request,'carga_empleados/leerEmpresa.html', contexto)


def eliminarEmpresa(request,nombre_empresa):
    empresa= empresa_terciarizada.objects.get(nombre=nombre_empresa)
    empresa.delete()

    empresa = empresa_terciarizada.objects.all()
    contexto = {'empresa': empresa}
    return render(request,"carga_empleados/leerEmpresa.html",contexto)

def editarEmpresa(request,nombre_empresa):
    empresa = empresa_terciarizada.objects.get(nombre=nombre_empresa)
    if request.method == 'POST':
        miFormulario = EmpresaFormularios(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empresa.nombre = informacion['nombre']
            empresa.razon_social = informacion['razon_social']
            empresa.cuit = informacion['cuit']

            empresa.save()

            return render(request,'carga_empleados/inicio.html')
    else:
        miFormulario = EmpresaFormularios(initial={'nombre':empresa.nombre,'razon_social':empresa.razon_social,'cuit':empresa.cuit})
    return render(request,'carga_empleados/editarEmpresa.html',{'miFormulario':miFormulario,'nombre_empresa':nombre_empresa})

# Clases Basadas en Vistas de Empleados


class EmpleadoList(ListView):
     model=Empleado
     template_name='carga_empleados/empleado_list.html'

class EmpleadoDetalle(DetailView):
     model= Empleado
     template_name = 'carga_empleados/empleadoDetalle.html'

class EmpleadoCreacion(CreateView):
     model = Empleado
     success_url = '/carga_empleados/empleado/list'
     fields = ['nombre','apellido','cargo']
    
class EmpleadoUpdate(UpdateView):
     model = Empleado
     success_url = '/carga_empleados/empleado/list'
     fields = ['nombre','apellido','cargo']
    
class EmpleadoDelete(DeleteView):
     model = Empleado
     success_url = '/carga_empleados/empleado/list'



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "carga_empleados/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "carga_empleados/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "carga_empleados/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "carga_empleados/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"carga_empleados/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"carga_empleados/registro.html" ,  {"form":form})



