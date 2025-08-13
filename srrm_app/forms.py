from django import forms
from .models import HospitalClinica, Medico, Paciente, RecetaMedica
from django.core.validators import RegexValidator

# --- Formulario Hospital/Clínica ---
class HospitalClinicaForm(forms.ModelForm):
    telefono_validator = RegexValidator(
        regex=r'^\+?[\d\s-]{10,13}$',
        message="Formato: +1234567890 o 123-456-7890"
    )
    
    telefono = forms.CharField(
        validators=[telefono_validator],
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 809-555-1234'})
    )

    rnc_validator = RegexValidator(
        regex=r'^\d{11}$',
        message="RNC debe tener 11 dígitos"
    )
    
    rnc = forms.CharField(
        validators=[rnc_validator],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = HospitalClinica
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# --- Formulario Médico ---
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'especializacion': forms.TextInput(attrs={'class': 'form-control'}),
            'firma_digital': forms.FileInput(attrs={'class': 'form-control'}),
            'hospitales': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }

# --- Formulario Paciente ---
class PacienteForm(forms.ModelForm):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opcional para menores'}),
            'seguro': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'medicos': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
            'hospitales': forms.SelectMultiple(attrs={'class': 'form-control select2'}),
        }

# --- Formulario Receta Médica ---
class RecetaMedicaForm(forms.ModelForm):
    class Meta:
        model = RecetaMedica
        fields = '__all__'
        widgets = {
            'hospital': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hora_descarga': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
