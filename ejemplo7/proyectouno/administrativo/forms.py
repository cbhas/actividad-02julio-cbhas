from django import forms
from administrativo.models import Estudiante, Modulo, Matricula

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_estudiante': forms.Select(attrs={'class': 'form-control'}),
        }

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = '__all__'
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}),
        }   

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'modulo': forms.Select(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MatriculaEditForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['comentario', 'costo']
