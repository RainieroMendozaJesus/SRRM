from django.urls import path , include
from . import views

app_name = "srrm_app"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('hospital/', views.mostrar_formulario_hospital, name='mostrar_formulario_hospital'),
    path('medico/', views.mostrar_formulario_medico, name='mostrar_formulario_medico'),
    path('paciente/', views.mostrar_formulario_paciente, name='mostrar_formulario_paciente'),
    path('receta/', views.mostrar_formulario_receta, name='mostrar_formulario_receta'),
]