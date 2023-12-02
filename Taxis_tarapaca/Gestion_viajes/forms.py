from django import forms
from .models import Usuario
from datetime import date

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'run', 'dv', 'apellido_p', 'apellido_m', 'nombre_usu', 'fecha_nacimiento', 'edad', 'email', 'prefijo', 'telefono', 'password', 'tipo_calle', 'direccion','genero']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date','max': str(date.today()),'required': 'required'}),
            'password': forms.PasswordInput(attrs={'required': 'required'}),
            'nombre_usu': forms.TextInput(attrs={'required': 'required'}),
            'dv': forms.TextInput(attrs={'pattern': '[0-9kK]'}),
            'nombre': forms.TextInput(attrs={'required': 'required'}),
            'apellido_p': forms.TextInput(attrs={'required': 'required'}),
            'apellido_m': forms.TextInput(attrs={'required': 'required'}),
            'run': forms.TextInput(attrs={'pattern': '[0-9]+', 'maxlength': '14'}),
            'telefono': forms.TextInput(attrs={'pattern':'[0-9]+','maxlength':'14'}),
            'email': forms.EmailInput(attrs={'required': 'required'}),
            'direccion': forms.TextInput(attrs={'required': 'required'}),
            'tipo_calle': forms.Select(attrs={'required': 'required'}),
        }
