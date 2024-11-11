from django.urls import path
from  materia_app import views


urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path('registrarMateria/',views.registrarMateria,name='registrarMateria'),
    path('seleccionarMateria/<codigo>',views.seleccionarMateria,name='seleccionarMateria'),
    path('editarMateria/',views.editarmateria,name='editarmateria'),
    path('borrarMateria/<codigo>',views.borrarMateria,name='borrarMateria'),
]
