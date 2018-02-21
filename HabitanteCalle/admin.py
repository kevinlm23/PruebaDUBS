from django.contrib import admin
from HabitanteCalle import models

class UsuarioAdmin(admin.ModelAdmin):
    list_display =('primer_nombre','segundo_nombre','primer_apellido',
                   'segundo_apellido','numero_documento','telefono_movil',
                   'pais_procedencia','departamento_procedencia','municipio_procedencia','ocupacion',
                   )
    filter_horizontal = ('educacion_desarrollo_humano',)
    search_fields = ('numero_documento','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido')
    fieldsets = (
        ('INFORMACION BASICA',{
            'fields':('primer_nombre','segundo_nombre','primer_apellido',
                   'segundo_apellido','tipo_documento_identidad','numero_documento','sexo','genero','fecha_nacimiento',)
        }),
        ('INFORMACION DE UBICACION Y CONTACTO', {
            'fields': ('lugar_nacimiento', 'telefono_fijo', 'telefono_movil',
                       'correo_electronico', 'pais_procedencia', 'departamento_procedencia', 'municipio_procedencia', 'zona_ubicacion',
                       'barrio','direccion','estrato','comuna','vereda','corregimiento',)
        }),
        ('INFORMACION DE NUCLEO FAMILIAR', {
            'fields': ('estado_civil', 'numero_hijos', 'cabeza_jefe_familia',)
        }),
        ('INFORMACION DE EDUCACION Y OCUPACION', {
            'fields': ('ocupacion', 'nivel_escolaridad', 'estudios_completos','educacion_desarrollo_humano',)
        }),
        ('INFORMACION COMUNITARIA', {
            'fields': ('etnia', 'comunidad_indigena', 'grupo', 'grupo_poblacional',)
        }),
        ('DISCAPACIDADES', {
            'fields': ('posee_discapacidad', 'cual_discapasidad',)
        }),
    )


class PaisAdmin(admin.ModelAdmin):
    list_display = ('pais',)
    ordering = ('pais',)
    search_fields = ('pais',)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('departamento',)
    ordering = ('departamento',)
    search_fields = ('departamento',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('municipio',)
    ordering = ('municipio',)
    search_fields = ('municipio',)

class EstudiosAdmin(admin.ModelAdmin):
    list_display = ('estudio',)
    ordering = ('estudio',)
    search_fields = ('estudio',)


admin.site.register(models.Usuario,UsuarioAdmin)
admin.site.register(models.Pais,PaisAdmin)
admin.site.register(models.Departamento,DepartamentoAdmin)
admin.site.register(models.Municipio,MunicipioAdmin)
admin.site.register(models.Estudios,EstudiosAdmin)