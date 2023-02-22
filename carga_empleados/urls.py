from django.urls import path
from carga_empleados import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('empleados', views.empleados,name="empleados"),
    path('empresa_terciarizada', views.empresa_terciarizada,name="empresa_terciarizada"),
    #path('empleadosFormularios',views.empleadosFormularios,name="empleados_Formularios")
    
]