from django.urls import path
from carga_empleados import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('empleados', views.empleados,name="empleados"),
    path('empresa_terciarizada', views.Empresa_terciarizada,name="empresa_terciarizada"),
    path('vehiculo_empresarial', views.Vehiculo_empresarial,name="vehiculo_empresarial"),
    #path('empleadosFormularios',views.empleadosFormularios,name="empleadosFormularios")
    path('leerEmpleados',views.leerempleados,name='LeerEmpleados'),
    path('eliminarEmpleado/<nombre_empleado>',views.eliminarEmpleado, name= "eliminarEmpleado"),
    path('editarEmpleado/<nombre_empleado>',views.editarEmpleado,name="editarEmpleado"),
    path('leerEmpresa',views.leerEmpresas,name='LeerEmpresa'),
    path('eliminarEmpresa/<nombre_empresa>',views.eliminarEmpresa,name='eliminarEmpresa'),
    path('editarEmpresa/<nombre_empresa>',views.editarEmpresa,name='editarEmpresa'),

    path('empleado/list',views.EmpleadoList.as_view(),name='list'),
    path(r'^(?P<pk>\d+)$',views.EmpleadoDetalle.as_view(),name='Detail'),
    path(r'^nuevo$',views.EmpleadoCreacion.as_view(),name = 'New'),
    path(r'^editar/(?P<pk>\d+)$',views.EmpleadoUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.EmpleadoDelete.as_view(),name='Delete'),
    path('login',views.login_request, name='Login'),
    path('register',views.register,name='Register'),
    path('logout', LogoutView.as_view(template_name='carga_empleados/logout.html'), name='Logout'),




]
