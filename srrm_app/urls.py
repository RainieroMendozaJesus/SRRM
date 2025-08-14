from django.urls import path , include
from . import views

app_name = "srrm_app"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
]