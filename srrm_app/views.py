from django.shortcuts import render

# Create your views here.

def index(request):
    """Muesta la pagina de Home"""
    return render(request, "srrm_app/index.html")


def servicios(request):
    """Muesta la pagina de servicios"""
    return render(request, "srrm_app/servicios.html")


def nosotros(request):
    """Muesta la pagina de servicios"""
    return render(request, "srrm_app/nosotros.html")
