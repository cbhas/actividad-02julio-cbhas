from django import forms
from administrativo.models import Estudiante, Modulo, Matricula

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']

class MatriculaEditForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['comentario', 'costo']
