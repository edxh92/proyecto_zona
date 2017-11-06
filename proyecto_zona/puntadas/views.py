from django.shortcuts import render
from django.contrib import messages
from .forms import EmpleadoForm
from puntadas.models import Empleado, Registro

def puntada_nueva(request):
    if request.method == "POST":
            formulario = EmpleadoForm(request.POST)
            if formulario.is_valid():
                empleado = empleado.objects.create(nombre=formulario.cleaned_data['nombre'], email = formulario.cleaned_data['email'],fecha_nacimiento =formulario.cleaned_data['fecha_nacimiento'])
                for puntada_id in request.POST.getlist('puntadas'):
                    puntada = Registro(actor_id=actor_id, empleado_id = empleado_id)
                    puntada.save()
                messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = EmpleadoForm()
    return render(request, 'puntadas/puntada_editar.html', {'formulario': formulario})
