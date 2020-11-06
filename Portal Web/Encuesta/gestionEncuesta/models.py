from django.db import models

import uuid # Requerida para las instancias de libros únicos
# Create your models here.
from django.db.models.aggregates import Count
from random import randint

#Hay que crear una clase por cada tabla en nuestra base de datos

class juegoEmparejarSinonimos(models.Model):
    palabra = models.CharField(max_length=150)
    sininimo_1 = models.CharField(max_length=150, help_text="Introduzca un sinonimo", null = True)
    sininimo_2 = models.CharField(max_length=150, help_text="Introduzca un sinonimo", null = True, blank = True)
    sininimo_3 = models.CharField(max_length=150, help_text="Introduzca un sinonimo", null = True, blank = True)

class juegoEmparejarAntonimos(models.Model):
    palabra = models.CharField(max_length=150)
    antonimo_1 = models.CharField(max_length=150, help_text="Introduzca un antonimo", null = True)
    antonimo_2 = models.CharField(max_length=150, help_text="Introduzca un antonimo", null = True, blank = True)
    antonimo_3 = models.CharField(max_length=150, help_text="Introduzca un antonimo", null = True, blank = True)

class reportUser(models.Model):
    #perfilEnc = models.CharField(max_length = 300)
    sexo = models.CharField(max_length = 10)
    rango_edad = models.CharField(max_length = 10)
    nacionalidad = models.CharField(max_length = 10)
    rasgo_nacional = models.CharField(max_length = 10)
    com_autonoma_nacimiento = models.CharField(max_length = 10)
    com_autonoma_actual = models.CharField(max_length = 10)
    com_autonoma_actual_anyos = models.CharField(max_length = 10)
    sector_trabajo = models.CharField(max_length = 10)
    renta = models.CharField(max_length = 10)
    estudios = models.CharField(max_length = 10)
    cultura = models.CharField(max_length = 10)
    frecuencia_libros = models.CharField(max_length = 300)
    tipos_libros = models.CharField(max_length = 300)
    uso_internet = models.CharField(max_length = 300)
    horas_estudio = models.CharField(max_length = 10)
    compras_internet = models.CharField(max_length = 10)
    dni_electronico = models.CharField(max_length = 10)
    renta_online = models.CharField(max_length = 10)
    blogs = models.CharField(max_length = 10)
    ocio_internet = models.CharField(max_length = 300)
    horas_ocio = models.CharField(max_length = 10)
    pregunta1 = models.BooleanField()
    pregunta2 = models.BooleanField()
    pregunta3 = models.BooleanField()
    pregunta4 = models.BooleanField()
    pregunta5 = models.BooleanField()
    emparejar_sinonimos = models.IntegerField(null = True, blank = True)
    emparejar_antonimos = models.IntegerField(null = True, blank = True)
    palabras_mezcladas = models.IntegerField(null = True, blank = True)
    momento = models.DateTimeField(auto_now_add = True, null = True)
    tiempo = models.TimeField(null= True)

    # def __str__(self):
    #     return ("El usuario con perfil de: "+ self.perfilEnc + " ha acabado la encuesta en el tiempo de: " + self.tiempo)

class preguntas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para la pregunta", editable=False)
    Niveles = models.TextChoices('Nivel', 'Nivel1 Nivel2 Nivel3 Nivel4 Nivel5')
    nivel = models.CharField(choices=Niveles.choices, max_length=10, help_text="Seleccione el nivel de la pregunta", null = True, blank = True)
    Tipos = models.TextChoices('Tipo', 'Booleana Clasica Rellenar')
    tipo = models.CharField(choices=Tipos.choices, max_length=10, help_text="Seleccione el tipo de la pregunta", null = True, blank = True)
    texto = models.CharField(max_length = 3000, default='Texto de lectura si procede', null = True, blank = True)
    pregunta = models.CharField(max_length = 3000, default='Ponga la pregunta aquí')
    opcion1 = models.CharField(max_length = 300, help_text="Introduzca la primera respuesta")
    opcion2 = models.CharField(max_length = 300, help_text="Introduzca la segunda respuesta")
    opcion3 = models.CharField(max_length = 300, help_text="Introduzca la tercera respuesta", null = True, blank = True)
    opcion4 = models.CharField(max_length = 300, help_text="Introduzca la cuarta respuesta", null = True, blank = True)
    respuesta_correcta = models.CharField(max_length = 300, help_text="Introduzca la respuesta correcta", null = True, blank = True)
    contador = models.IntegerField(null = True, blank = True, default = 0)
    fallo = models.IntegerField(null = True, blank = True, default = 0)

class reportPreguntas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para el report", editable=False)
    preguntas = models.ForeignKey(preguntas, on_delete=models.CASCADE)
    contador = models.IntegerField(null = True, blank = True, default = 0)
    fallos = models.IntegerField(null = True, blank = True, default = 0)

#class reportEncuesta(models.Model):
# hay que crear el modelo de reports de las encuestas para 
# saber que preguntas han caido en cada encuesta y también
# poder sacar datos y/o conclusiones de ello    
