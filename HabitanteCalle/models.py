from __future__ import unicode_literals

from django.db import models
TIPO_DOCUMENTO_CHOICES=(
    ('Cédula de Ciudadanía','Cédula de Ciudadanía'),
    ('Cédula de Extranjería', 'Cédula de Extranjería'),
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
ESTUDIOS_DESARROLLO_HUMANO=(
    ('Educaccion para el Trabajo','Educaccion para el Trabajo'),
    ('Desarrollo Humano','Desarrollo Humano'),
)
ETNIA=(
    ('Afro','Afro'),
    ('Mestizo','Mestizo'),
    ('Indígena','Indígena'),
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
    ('Física','Física')
)

class Pais(models.Model):
    pais=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.pais

class Departamento(models.Model):
    departamento=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.departamento

class Municipio(models.Model):
    municipio=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.municipio

class Usuario(models.Model):
    primer_nombre=models.CharField(max_length=60)
    segundo_nombre = models.CharField(max_length=60,blank=True,null=True)
    primer_apellido = models.CharField(max_length=60)
    segundo_apellido = models.CharField(max_length=60,blank=True,null=True)
    tipo_documento_identidad=models.CharField(choices=TIPO_DOCUMENTO_CHOICES,max_length=100)
    numero_documento=models.CharField(max_length=20)
    sexo=models.CharField(choices=SEXO,max_length=100)
    genero=models.CharField(choices=GENERO,blank=True,null=True,max_length=100)
    fecha_nacimiento=models.DateField(blank=True,null=True)
    lugar_nacimiento=models.CharField(max_length=60,blank=True,null=True)
    telefono_fijo=models.CharField(max_length=20, blank=True,null=True)
    telefono_movil = models.CharField(max_length=20, blank=True,null=True)
    correo_electronico=models.EmailField(max_length=60,blank=True,null=True)
    pais_procedencia=models.ForeignKey(Pais,on_delete=models.CASCADE,null=True,blank=True)
    departamento_procedencia=models.ForeignKey(Departamento,on_delete=models.CASCADE,null=True,blank=True)
    municipio_procedencia=models.ForeignKey(Municipio,on_delete=models.CASCADE,null=True,blank=True)
    zona_ubicacion=models.CharField(choices=UBICACION,blank=True,null=True,max_length=100)
    barrio=models.CharField(max_length=60,blank=True)
    direccion=models.CharField(max_length=60,blank=True)
    estrato=models.CharField(max_length=20,blank=True)
    comuna =models.CharField(max_length=60,blank=True)
    vereda=models.CharField(max_length=60,blank=True)
    corregimiento=models.CharField(max_length=60,blank=True)
    estado_civil=models.CharField(choices=ESTADO_CIVIL,blank=True,null=True,max_length=100)
    numero_hijos=models.CharField(max_length=20,blank=True)
    cabeza_jefe_familia=models.CharField(choices=CABEZA_JEFE_DE_FAMILIA,blank=True,null=True,max_length=100,verbose_name='Es cabeza de familia o jefe(a) de hogar')
    ocupacion=models.CharField(choices=OCUPACION,blank=True,null=True,max_length=100)
    nivel_escolaridad=models.CharField(choices=NIVEL_ESCOLARIDAD,blank=True,null=True,max_length=100)
    estudios_completos=models.BooleanField(blank=True,verbose_name='Realizó sus estudios de manera completa')
    educacion_desarrollo_humano=models.CharField(choices=ESTUDIOS_DESARROLLO_HUMANO,blank=True,null=True,max_length=100,verbose_name='Ha llevado a cabo alguno de estos estudios de Educación para el Trabajo y el Desarrollo Humano')
    etnia=models.CharField(choices=ETNIA,null=True,blank=True,max_length=100,verbose_name='Autoreconocimiento étnico')
    comunidad_indigena=models.CharField(max_length=60,blank=True,null=True,verbose_name='Si su respuesta es indígena indique a qué comunidad pertenece')
    grupo=models.CharField(choices=PERTENECE_GRUPO,blank=True,null=True,max_length=100,verbose_name='Pertenece actualmente a alguno de estos grupos')
    grupo_poblacional=models.CharField(max_length=100,blank=True,null=True,verbose_name='cuál?')
    posee_discapacidad=models.BooleanField(blank=True,verbose_name='Posee alguna discapacidad')
    cual_discapasidad=models.CharField(choices=DISCAPACIDAD,blank=True,null=True,max_length=100,verbose_name='Cuál?')


