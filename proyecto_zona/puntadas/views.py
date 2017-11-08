from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import EmpleadoForm, PuntadaForm
# from django.utils import timezone
from puntadas.models import Empleado, Registro, Puntada

def inicio(request):
    empleado = Registro.objects.filter(empleado_id=2)
    variable=[]
    for empleado in empleado:
        puntadas=Puntada.objects.filter(pk=empleado.puntada_id)
        variable.append(puntadas)
    return render(request,'lista.html',{'variable':variable})

@login_required
def puntada_nueva(request):
   if request.method == "POST":
      formulario = EmpleadoForm(request.POST)
      if formulario.is_valid():
         empleado = Empleado.objects.create(nombre=formulario.cleaned_data['nombre'], email = formulario.cleaned_data['email'],fecha_nacimiento =formulario.cleaned_data['fecha_nacimiento'])
         for puntada_id in request.POST.getlist('puntadas'):
             puntada = Registro(puntada_id = puntada_id, empleado_id = empleado.id)
             puntada.save()
      return redirect('/')
   else:
       formulario = EmpleadoForm()
   return render(request, 'puntada_edit.html', {'formulario': formulario})

def lista_puntadas(request):
    puntada=Puntada.objects.all()
    return render(request,'lista_puntadas.html',{'puntada':puntada})

@login_required
def puntada_new(request):
   if request.method == "POST":
      formulario = PuntadaForm(request.POST)
      if formulario.is_valid():
         puntada = Puntada.objects.create(descripcion=formulario.cleaned_data['descripcion'], costo_puntada = formulario.cleaned_data['costo_puntada'],status =formulario.cleaned_data['status'])
      return redirect('/')
   else:
       formulario = PuntadaForm()
   return render(request, 'puntada_new.html', {'formulario': formulario})

@login_required
def puntadas_remove(request, pk):
    puntda = get_object_or_404(Puntada, pk=pk)
    puntda.delete()
    return redirect('/')
