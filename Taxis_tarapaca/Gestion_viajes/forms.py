from django import forms
from .models import Usuario, Reserva, TiposCalle
from datetime import date, datetime

class UsuarioForm(forms.ModelForm):
    
    genero = forms.ChoiceField(choices=[('M','Masculino'),('F','Femenino'),('otro','Otro'),('prefiero_no_contestar','Prefiero No Contestar')], widget=forms.Select(attrs={}))
    
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
        
class ReservaUsuarioForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['tipo_origen'].queryset = TiposCalle.objects.exclude(nombre='Sin calle')
            
            self.fields['tipo_destino'].queryset = TiposCalle.objects.exclude(nombre='Sin calle')
    
    class Meta:
        model = Reserva
        fields = ['origen','tipo_origen','destino','tipo_destino','cantidad_pasajeros','descripcion','fecha_reserva','medio_contacto','contacto','prefijo','region','comuna','ciudad','region_destino','ciudad_destino','comuna_destino','numero_origen','numero_destino']
        
        widgets = {
            'cantidad_pasajeros': forms.NumberInput(attrs={'min': 1,'required':'required'}),
            'origen': forms.TextInput(attrs={'required':'required'}),
            'tipo_origen': forms.Select(attrs={'required':'required'}),
            'destino': forms.TextInput(attrs={'required':'required'}),
            'tipo_destino': forms.Select(attrs={'required':'required'}),
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local', 'min': str(datetime.now().strftime('%Y-%m-%dT%H:%M')), 'required': 'required'}),
            'medio_contacto': forms.Select(attrs={}),
            'contacto': forms.TextInput(attrs={'hidden':'true'}),
            'prefijo': forms.Select(attrs={'hidden':'true'})
        }
        