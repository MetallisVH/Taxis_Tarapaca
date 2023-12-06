from django import forms
from .models import *
from datetime import date, datetime

class UsuarioForm(forms.ModelForm):
    
    genero = forms.ChoiceField(choices=[('M','Masculino'),('F','Femenino'),('otro','Otro'),('prefiero_no_contestar','Prefiero No Contestar')], widget=forms.Select(attrs={}))
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'run', 'dv', 'apellido_p', 'apellido_m', 'nombre_usu', 'fecha_nacimiento', 'edad', 'email', 'prefijo', 'telefono', 'password', 'tipo_calle', 'direccion','genero','tipo']
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
        
class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = ['monto_tarifa','region','ciudad','comuna','region_destino','ciudad_destino','comuna_destino','fecha_viaje']

        widgets = {
            'region': forms.Select(attrs={'required':'required'}),
            'ciudad': forms.Select(attrs={'hidden':'true'}),
            'comuna': forms.Select(attrs={'hidden':'true'}),
            'region_destino': forms.Select(attrs={'required':'required'}),
            'ciudad_destino': forms.Select(attrs={'hidden':'true'}),
            'comuna_destino': forms.Select(attrs={'hidden':'true'}),
            'fecha_viaje': forms.DateInput(attrs={'type': 'date','min': str(date.today())}),
        }
        
class ReclamoForm(forms.ModelForm):
    class Meta:
        model = Reclamo
        fields = ['tipo_reclamo','autor','reclamacion','estado','anulado','tipo_contacto', 'prefijo','contacto','viaje','reserva', 'motivo_anulacion','deleted_at','created_at']
        
        widgets = {
            'tipo_reclamo': forms.Select(attrs={'required':'required'}),
            'contacto': forms.TextInput(attrs={'hidden':'true','required':'required'}),
            'prefijo': forms.Select(attrs={'hidden':'true'}),
            'tipo_contacto': forms.Select(attrs={'required':'required'}),
        }

class TaxistaForm(forms.ModelForm):
    
    genero = forms.ChoiceField(choices=[('','Seleccione un genero'),('M','Masculino'),('F','Femenino'),('otro','Otro'),('prefiero_no_contestar','Prefiero No Contestar')], widget=forms.Select(attrs={}))
    
    class Meta:
        model = Taxista
        fields = ['nombre', 'apellido_p', 'apellido_m', 'genero', 'secretaria_encargada', 'run', 'dv', 'estado']
        
        widgets = {
            'nombre': forms.TextInput(attrs={'required': True}),
            'apellido_p': forms.TextInput(attrs={'required': True}),
            'apellido_m': forms.TextInput(attrs={'required': True}),
            'run': forms.NumberInput(attrs={}),
            'dv': forms.TextInput(attrs={}),
        }