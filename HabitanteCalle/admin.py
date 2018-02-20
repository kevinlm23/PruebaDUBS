from django.contrib import admin
from HabitanteCalle import models

class UsuarioAdmin(admin.ModelAdmin):
    list_display =('primer_nombre','segundo_nombre','primer_apellido',
                   'segundo_apellido','numero_documento','telefono_movil',
                   'pais_procedencia','departamento_procedencia','municipio_procedencia','ocupacion',
                   )


class PaisAdmin(admin.ModelAdmin):
    list_display = ('pais',)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('departamento',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('municipio',)

admin.site.register(models.Usuario,UsuarioAdmin)
admin.site.register(models.Pais,PaisAdmin)
admin.site.register(models.Departamento,DepartamentoAdmin)
admin.site.register(models.Municipio,MunicipioAdmin)