from django.urls import path
from carga_empleados import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('empleados', views.empleados,name="empleados"),
    path('empresa_terciarizada', views.empresa_terciarizada,name="empresa_terciarizada"),
    path('vehiculo_empresarial', views.vehiculo_empresarial,name="vehiculo_empresarial"),
    #path('empleadosFormularios',views.empleadosFormularios,name="empleadosFormularios")
    path('leerEmpleados',views.leerempleados,name='LeerEmpleados'),
    path('eliminarEmpleado/<empleado_nombre>',views.eliminarEmpleado, name= "eliminarEmpleado"),
    path('editarEmpleado/<empleado_nombre>',views.editarEmpleado,name="editarEmpleado"),

]