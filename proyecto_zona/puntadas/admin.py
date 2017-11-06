from django.contrib import admin
from puntadas.models import Puntada, PuntadaAdmin, Empleado, EmpleadoAdmin
admin.site.register(Puntada,PuntadaAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
# Register your models here.
