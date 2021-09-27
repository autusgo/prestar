from django.contrib import admin

# Register your models here.

from simulador.models import Administrativo,Emprendedor,Emprendimiento,Microcredito,Promotor

admin.site.register(Administrativo)
admin.site.register(Emprendedor)
admin.site.register(Emprendimiento)
admin.site.register(Microcredito)
admin.site.register(Promotor)