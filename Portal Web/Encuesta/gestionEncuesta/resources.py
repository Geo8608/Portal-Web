#from import_export import resources
import import_export
from .models import preguntas, reportPreguntas, reportUser

class preguntasResource(import_export.resources.ModelResource):
    class Meta:
        model = preguntas
        import_id_fields = ["nivel","tipo", "texto", "pregunta", "opcion1", "opcion2", "opcion3",
                             "opcion4", "respuesta_correcta", "contador", "fallo"]
        fields = ("nivel","tipo", "texto", "pregunta", "opcion1", "opcion2", "opcion3",
                  "opcion4", "respuesta_correcta", "contador", "fallo")

class reportPreguntasResource(import_export.resources.ModelResource):
    class Meta:
        model = reportPreguntas


class reportUserResource(import_export.resources.ModelResource):
    class Meta:
        model = reportUser