from django import forms
from .models import Empleado, Puntada

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('nombre','email','fecha_nacimiento','puntadas')

def __init__ (self, *args, **kwargs):
    super(Empleado, self).__init__(*args, **kwargs)
    self.fields["puntadas"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["puntadas"].help_text = "Ingrese los Actores que participaron en la película"
    self.fields["puntadas"].queryset = Puntada.objects.all()

class PuntadaForm(forms.ModelForm):
    class Meta:
        model=Puntada
        fields=('descripcion','costo_puntada','status')
