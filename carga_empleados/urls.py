from django.urls import path
from carga_empleados import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('empleados', views.empleados),
    path('empresa_terciarizada', views.empresa_terciarizada),
    
]