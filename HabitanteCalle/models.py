from __future__ import unicode_literals

from django.db import models
TIPO_DOCUMENTO_CHOICES=(
    ('Cedula de Ciudadania','Cedula de Ciudadania'),
    ('Cedula de Extranjeria', 'Cedula de Extranjeria'),
    ('Tarjeta de Identidad','Tarjeta de Identidad'),
)
SEXO=(
    ('Masculino','Masculino'),
    ('Femenino','Femenino'),
)
GENERO=(
    ('Hombre','Hombre'),
    ('Mujer','Mujer'),
)

UBICACION=(
    ('Norte','Norte'),
    ('Sur','Sur'),
    ('Oriente','Oriente'),
    ('Occidente','Occidnete'),
)
ESTADO_CIVIL=(
    ('Soltero','Soltero'),
    ('Casado','Casado'),
    ('Union Libre','Union Libre'),
)
CABEZA_JEFE_DE_FAMILIA=(
    ('Jefe','Jefe'),
    ('Cabeza','Cabeza'),

)
OCUPACION=(
    ('Estudiante','Estudiante'),
    ('Independiente','Independiente'),
    ('Asalariado','Asalariado'),
    ('Estudiante y Asalariado','Estudiante y Asalariado'),
)
NIVEL_ESCOLARIDAD=(
    ('Primaria','Primaria'),
    ('Secundaria','Secundaria'),
    ('Universitaria','Universitaria'),
)

ETNIA=(
    ('Afro','Afro'),
    ('Mestizo','Mestizo'),
    ('Indigena','Indigena'),
)
PERTENECE_GRUPO=(
    ('Poblacionales','Poblacionales'),
    ('Comunitarios','Comunitarios'),
    ('Sociales','Sociales'),
)
DISCAPACIDAD=(
    ('Auditiva','Auditiva'),
    ('Visual','Visual'),
    ('Cognitiva','Cognitiva'),
    ('Fisica','Fisica')
)

class Pais(models.Model):
    pais=models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.pais

class Departamento(models.Model):
    departamento=models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.departamento

class Municipio(models.Model):
    municipio=models.CharField(max_length=100,blank=True,null=True)
    def __unicode__(self):
        return self.municipio

class Estudios(models.Model):
    estudio=models.CharField(max_length=100,blank=True,null=True,)
    def __unicode__(self):
        return self.estudio

class Usuario(models.Model):
    primer_nombre=models.CharField(verbose_name='Pimer Nombre',max_length=60)
    segundo_nombre = models.CharField(verbose_name='Segundo Nombre',max_length=60,blank=True,null=True)
    primer_apellido = models.CharField(verbose_name='Pimer Apellido',max_length=60)
    segundo_apellido = models.CharField(verbose_name='Segundo Apellido',max_length=60,blank=True,null=True)
    tipo_documento_identidad=models.CharField(verbose_name='Tipo de Documento de Identidad',choices=TIPO_DOCUMENTO_CHOICES,max_length=100)
    numero_documento=models.CharField(verbose_name='Numero de Documento de Identidad',max_length=20)
    sexo=models.CharField(verbose_name='Sexo',choices=SEXO,max_length=100)
    genero=models.CharField(verbose_name='Genero',choices=GENERO,blank=True,null=True,max_length=100)
    fecha_nacimiento=models.DateField(verbose_name='Fecha de Nacimiento',blank=True,null=True)
    lugar_nacimiento=models.CharField(verbose_name='Lugar de Nacimiento',max_length=60,blank=True,null=True)
    telefono_fijo=models.CharField(verbose_name='Telefono Fijo',max_length=20, blank=True,null=True)
    telefono_movil = models.CharField(verbose_name='Telefono Movil',max_length=20, blank=True,null=True)
    correo_electronico=models.EmailField(verbose_name='Correo Electronico',max_length=60,blank=True,null=True)
    pais_procedencia=models.ForeignKey(Pais,verbose_name='Pais de Prosedencia',on_delete=models.CASCADE,null=True,blank=True)
    departamento_procedencia=models.ForeignKey(Departamento,verbose_name='Departamento de Prosedencia',on_delete=models.CASCADE,null=True,blank=True)
    municipio_procedencia=models.ForeignKey(Municipio,verbose_name='Municipio de Prosecendencia',on_delete=models.CASCADE,null=True,blank=True)
    zona_ubicacion=models.CharField(verbose_name='Zona de Ubicacion',choices=UBICACION,blank=True,null=True,max_length=100)
    barrio=models.CharField(max_length=60,blank=True)
    direccion=models.CharField(max_length=60,blank=True)
    estrato=models.CharField(max_length=20,blank=True)
    comuna =models.CharField(max_length=60,blank=True)
    vereda=models.CharField(max_length=60,blank=True)
    corregimiento=models.CharField(max_length=60,blank=True)
    estado_civil=models.CharField(verbose_name='Estado Civil',choices=ESTADO_CIVIL,blank=True,null=True,max_length=100)
    numero_hijos=models.CharField(verbose_name='Numero de Hijos',max_length=20,blank=True)
    cabeza_jefe_familia=models.CharField(choices=CABEZA_JEFE_DE_FAMILIA,blank=True,null=True,max_length=100,verbose_name='Es cabeza de familia o jefe(a) de hogar')
    ocupacion=models.CharField(choices=OCUPACION,blank=True,null=True,max_length=100)
    nivel_escolaridad=models.CharField(verbose_name='Nivel de Escolaridad',choices=NIVEL_ESCOLARIDAD,blank=True,null=True,max_length=100)
    estudios_completos=models.BooleanField(blank=True,verbose_name='Realizo sus estudios de manera completa')
    educacion_desarrollo_humano=models.ManyToManyField(Estudios,blank=True,max_length=100,verbose_name='Ha llevado a cabo alguno de estos estudios de Educacion para el Trabajo y el Desarrollo Humano')
    etnia=models.CharField(choices=ETNIA,null=True,blank=True,max_length=100,verbose_name='Autoreconocimiento etnico')
    comunidad_indigena=models.CharField(max_length=60,blank=True,null=True,verbose_name='Si su respuesta es indigena indique a quee comunidad pertenece')
    grupo=models.CharField(choices=PERTENECE_GRUPO,blank=True,null=True,max_length=100,verbose_name='Pertenece actualmente a alguno de estos grupos')
    grupo_poblacional=models.CharField(max_length=100,blank=True,null=True,verbose_name='cual?')
    posee_discapacidad=models.BooleanField(blank=True,verbose_name='Posee alguna discapacidad')
    cual_discapasidad=models.CharField(choices=DISCAPACIDAD,blank=True,null=True,max_length=100,verbose_name='Cual?')

    def __unicode__(self):
        return self.numero_documento


