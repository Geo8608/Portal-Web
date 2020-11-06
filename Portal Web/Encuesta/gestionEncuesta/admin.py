from django.contrib import admin

# Register your models here.

from gestionEncuesta.models import juegoEmparejarSinonimos, juegoEmparejarAntonimos
from gestionEncuesta.models import preguntas, reportPreguntas, reportUser

from import_export.admin import ImportExportModelAdmin
from .resources import preguntasResource, reportPreguntasResource, reportUserResource

"""Empezamos creado la clase de sininimos para poder
   gestionarla desde la página de administrador """
class juegoSinonimosAdmin(admin.ModelAdmin):
    # mostrar varias columnas con información de la tabla
    list_display = ("palabra", "sininimo_1", "sininimo_2", "sininimo_3")
    # activar el buscador para las columnsa especificadas
    search_fields = ("palabra",) 

#Mismo tipo de clase pero los antonimos
class juegoAntonimosAdmin(admin.ModelAdmin):
    # mostrar varias columnas con información de la tabla
    list_display = ("palabra", "antonimo_1", "antonimo_2", "antonimo_3")
    # activar el buscador para las columnsa especificadas
    search_fields = ("palabra",) 
    #list_filter = ( "palabra", )


#Clase para poder gestionar las preguntas de los distinos niveles (1-5)
@admin.register(reportUser)
class reportUserAdmin(ImportExportModelAdmin):
    readonly_fields = ("sexo", "rango_edad", "nacionalidad", "rasgo_nacional", "com_autonoma_nacimiento",
                       "com_autonoma_actual", "com_autonoma_actual_anyos", "sector_trabajo", "renta", 
                       "estudios", "cultura", "frecuencia_libros", "tipos_libros", "uso_internet",
                       "horas_estudio", "compras_internet", "dni_electronico", "renta_online",
                       "blogs", "ocio_internet", "horas_ocio", "pregunta1", "pregunta2", "pregunta3",
                       "pregunta4", "pregunta5", "emparejar_sinonimos", "emparejar_antonimos",
                       "palabras_mezcladas", "momento", "tiempo" )
    resource_class = reportUserResource
    #list_filter = ("perfilEnc",)
    #filtro parecido a las migas de pan con las fechas
    #date_hierarchy = "fecha"  


@admin.register(preguntas)
class preguntasAdmin(ImportExportModelAdmin):
    list_display = ("nivel","tipo", "texto", "pregunta", "opcion1", "opcion2", "opcion3",
                    "opcion4", "respuesta_correcta", "contador", "fallo")
    resource_class = preguntasResource

@admin.register(reportPreguntas)
class reportsPreguntasAdmin(ImportExportModelAdmin):
    readonly_fields = ("preguntas", "contador", "fallos")
    resource_class = reportPreguntasResource
    """ Sería interesante mostrar aquí directamente la información en forma de gráficas
        Tipos de gráficas
        1. Fallos acumulados por nivel
        2. Preguntas más falladas
        3. Tarta de queso con los aciertos y los fallos - totales y por nivel
        4. Palabras más falladas 
        5.
        6.
     """

admin.site.site_header = "Panel de Administración"

# Registarmos las clases en la página de admin para que las podamos gestionar desd ahí
admin.site.register(juegoEmparejarSinonimos, juegoSinonimosAdmin)
admin.site.register(juegoEmparejarAntonimos, juegoAntonimosAdmin)
