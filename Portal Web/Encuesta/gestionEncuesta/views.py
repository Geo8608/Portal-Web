from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
from gestionEncuesta.models import juegoEmparejarSinonimos, juegoEmparejarAntonimos
from gestionEncuesta.models import preguntas, reportPreguntas, reportUser
from gestionEncuesta.separador import silabizer
import pylint
import random
import secrets

# Create your views here.

#Función auxiliar para guardar los datos de un encuestrado
def save(perfil, data, momento):
    tiempo = datetime.now - momento
    encuestado = finalEncuesta(perfilEnc = perfil, resultado = data, momento = momento, tiempo = tiempo)
    encuestado.save()

# Función para definir el perfil del usuario con las respuestas de la encuesta
def perfil(data):

    return perfil


def index(request):
    
    return render(request, "index.html" )

####Funcion que separa las letras de una palabra

def jumbled(word):
    # sample() method shuffling the characters of the word 
    random_word = random.sample(word, len(word)) 
    print(random_word)
    # join() method join the elements 
    # of the iterator(e.g. list) with particular character . 
    jumbled = ' '.join(random_word) 

    return jumbled.upper()

#Función que separa en silabas una palabra
def silabas(word):
    silaba = silabizer()
    random_word = silaba(word)
    random.shuffle(random_word)
    palabra = ' '.join([str(item) for item in random_word ])
    return palabra.upper()

def base(request):
    """Con la linea de abajo le decimos a Django que no traiga de la pagina web datos
        que tenemos de cada modelo de la BB.DD""" 
    sinonimo1 = juegoEmparejarSinonimos.objects.order_by("?").first()
    sinonimo2 = juegoEmparejarSinonimos.objects.order_by("?").first()
    sinonimo3 = juegoEmparejarSinonimos.objects.order_by("?").first()
    sinonimo4 = juegoEmparejarSinonimos.objects.order_by("?").first()
    antonimo1 = juegoEmparejarAntonimos.objects.order_by("?").first()
    antonimo2 = juegoEmparejarAntonimos.objects.order_by("?").first()
    antonimo3 = juegoEmparejarAntonimos.objects.order_by("?").first()
    antonimo4 = juegoEmparejarAntonimos.objects.order_by("?").first()
    #resultado = finalEncuesta.objects.all()
    random1 = silabas(juegoEmparejarSinonimos.objects.order_by("?").first().palabra)
    random2 = silabas(juegoEmparejarSinonimos.objects.order_by("?").first().palabra)
    random3 = silabas(juegoEmparejarSinonimos.objects.order_by("?").first().palabra)
    nivel1 = preguntas.objects.filter(nivel = "Nivel1").order_by("?").first()
    nivel2 = preguntas.objects.filter(nivel = "Nivel2").order_by("?").first()
    nivel3 = preguntas.objects.filter(nivel = "Nivel3").order_by("?").first()
    nivel4 = preguntas.objects.filter(nivel = "Nivel4").order_by("?").first()
    nivel5 = preguntas.objects.filter(nivel = "Nivel5").order_by("?").first()


    if request.method == 'POST': 
        aux = reportUser()

        aux.sexo = request.POST.get('genero')   
        print(request.POST.get('genero'))

        aux.rango_edad = request.POST.get('edad')
        print(request.POST.get('edad'))

        aux.nacionalidad = request.POST.get('nacionalidad')
        print(request.POST.get('nacionalidad'))

        aux.rasgo_nacional = request.POST.get('rasgo')
        print(request.POST.get('rasgo'))

        aux.com_autonoma_nacimiento = request.POST.get('com_nacimiento')
        print(request.POST.get('com_nacimiento'))

        aux.com_autonoma_actual = request.POST.get('com_actual')
        print(request.POST.get('com_actual'))

        aux.com_autonoma_actual_anyos = request.POST.get('anyos_actual')
        print(request.POST.get('anyos_actual'))

        aux.sector_trabajo = request.POST.get('profesion')
        print(request.POST.get('profesion'))

        aux.renta = request.POST.get('renta')
        print(request.POST.get('renta'))

        aux.estudios = request.POST.get('estudios')
        print(request.POST.get('estudios'))

        aux.cultura = request.POST.get('cultura')
        print(request.POST.get('cultura'))

        aux.frecuencia_libros = request.POST.get('frecuencia_libros')
        print(request.POST.get('frecuencia_libros'))

        aux.tipos_libros = {'libros_impresos': request.POST.getlist('libros_impresos')}
        print(request.POST.getlist('libros_impresos'))

        aux.tipos_libros['libros_digitales'] = request.POST.getlist('libros_digital')
        print(request.POST.getlist('libros_digital'))

        aux.uso_internet = request.POST.getlist('uso_internet')
        print(request.POST.getlist('uso_internet'))

        aux.horas_estudio = request.POST.get('horas_estudio')
        print(request.POST.get('horas_estudio'))

        aux.compras_internet = request.POST.get('compra_int')
        print(request.POST.get('compra_int'))

        aux.dni_electronico = request.POST.get('dni')
        print(request.POST.get('dni'))

        aux.renta_online = request.POST.get('declaracion')
        print(request.POST.get('declaracion'))

        aux.blogs = request.POST.get('blogs')
        print(request.POST.get('blogs'))

        aux.ocio_internet = request.POST.getlist('ocio_red')
        print(request.POST.getlist('ocio_red'))

        aux.horas_internet = request.POST.get('horas_red')
        print(request.POST.get('horas_red'))

        aux.pregunta1 = True
        print(request.POST.get('nivel1'))
        aux_pregunta1 = reportPreguntas()
        aux_pregunta1.preguntas = nivel1
        aux_pregunta1.contador = aux_pregunta1.contador + 1
        aux_pregunta1.fallos = aux_pregunta1.contador + 1


        aux.pregunta2 = False
        print(request.POST.get('nivel2'))
        aux_pregunta2 = reportPreguntas()
        aux_pregunta2.preguntas = nivel2
        aux_pregunta2.contador = aux_pregunta2.contador + 1
        aux_pregunta2.fallos = aux_pregunta2.contador + 1


        aux.pregunta3 = True
        print(request.POST.get('nivel3'))
        aux_pregunta3 = reportPreguntas()
        aux_pregunta3.preguntas = nivel3
        aux_pregunta3.contador = aux_pregunta3.contador + 1
        aux_pregunta3.fallos = aux_pregunta3.contador + 1


        aux.pregunta4 = True
        print(request.POST.get('nivel4'))
        aux_pregunta4 = reportPreguntas()
        aux_pregunta4.preguntas = nivel1
        aux_pregunta4.contador = aux_pregunta4.contador + 1
        aux_pregunta4.fallos = aux_pregunta4.contador + 1


        aux.pregunta5 = True
        print(request.POST.get('nivel5'))
        aux_pregunta5 = reportPreguntas()
        aux_pregunta5.preguntas = nivel5
        aux_pregunta5.contador = aux_pregunta5.contador + 1
        aux_pregunta5.fallos = aux_pregunta5.contador + 1


        print(request.POST.get('random1'))

        print(request.POST.get('random2'))

        print(request.POST.get('random3'))
        aux.palabras_mezcladas = 3
        aux.tiempo = datetime.now()
        aux.save()

    context = {"sinonimo1":sinonimo1, "sinonimo2":sinonimo2, "sinonimo3":sinonimo3, "sinonimo4":sinonimo4, 
                "antonimo1": antonimo1, "antonimo2": antonimo2, "antonimo3": antonimo3, "antonimo4": antonimo4,
                "random1": random1, "random2": random2, "random3": random3, "nivel1": nivel1,
                "nivel2": nivel2, "nivel3": nivel3, "nivel4": nivel4, "nivel5": nivel5 }
 
    return render(request, "base.html", context )


# def saveData(request):
#     reporte = report()
#     pass


def thanks(request):
    
    return render(request, "thanks.html" )

def about(request):
    
    return render(request, "about.html" )
