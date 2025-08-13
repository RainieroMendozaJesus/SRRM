from django.shortcuts import render
from .forms import HospitalClinicaForm, MedicoForm, PacienteForm, RecetaMedicaForm

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


def mostrar_formulario_hospital(request):
    form = HospitalClinicaForm()
    return render(request, 'srrm_app/hospital.html', {'form': form})

def mostrar_formulario_medico(request):
    form = MedicoForm()
    return render(request, 'srrm_app/medico.html', {'form': form})

def mostrar_formulario_paciente(request):
    form = PacienteForm()
    return render(request, 'srrm_app/paciente.html', {'form': form})

def mostrar_formulario_receta(request):
    form = RecetaMedicaForm()
    return render(request, 'srrm_app/receta.html', {'form': form})