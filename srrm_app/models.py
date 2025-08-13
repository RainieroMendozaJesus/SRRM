from django.db import models

class HospitalClinica(models.Model):
    id_hc = models.AutoField(primary_key=True)
    rnc = models.CharField(max_length=11)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    id_medico = models.AutoField(primary_key=True)
    # Relación M:M con HospitalClinica
    hospitales = models.ManyToManyField(
        HospitalClinica,
        related_name='medicos',
        verbose_name='Hospitales/Clínicas donde trabaja'
    )
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=13)
    email = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    especializacion = models.CharField(max_length=50)
    firma_digital = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    
    id_paciente = models.AutoField(primary_key=True)
    # Relación M:M con Médicos
    medicos = models.ManyToManyField(
        Medico,
        related_name='pacientes',
        verbose_name='Médicos que atienden al paciente'
    )
    # Relación M:M con Hospitales/Clínicas
    hospitales = models.ManyToManyField(
        HospitalClinica,
        related_name='pacientes_hospital',
        verbose_name='Hospitales/Clínicas donde está registrado'
    )
    nombre = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    direccion = models.CharField(max_length=100)
    cedula = models.CharField(max_length=13, blank=True, null=True)
    seguro = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)

    def __str__(self):
        return self.nombre

class RecetaMedica(models.Model):
    id_receta = models.AutoField(primary_key=True)
    # Cada receta pertenece a un hospital específico
    hospital = models.ForeignKey(
        HospitalClinica, 
        on_delete=models.CASCADE,
        related_name='recetas'
    )
    # Cada receta es emitida por un médico específico
    medico = models.ForeignKey(
        Medico, 
        on_delete=models.CASCADE,
        related_name='recetas_emitidas'
    )
    # Cada receta es para un paciente específico
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='recetas_recibidas'
    )
    descripcion = models.CharField(max_length=255)
    hora_descarga = models.DateTimeField()

    def __str__(self):
        return f'Receta {self.id_receta} - {self.paciente.nombre}'