from django.contrib import admin
from .models import HospitalClinica, Medico, Paciente, RecetaMedica
# Register your models here.

admin.site.register(HospitalClinica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(RecetaMedica)
