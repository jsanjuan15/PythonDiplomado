from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Lista(models.Model):
    titulo_lista = models.CharField(max_length=200, unique=True)
    fecha_lista = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_lista

@python_2_unicode_compatible  # only if you need to support Python 2
class Tareas(models.Model):
    id_lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    titulo_tarea = models.CharField(max_length=200, unique=True)
    estado_tarea = models.BooleanField(default=False)
    descripcion_tarea = models.TextField(help_text='Describe la Tarea', blank=True)
    fecha_creacion_tarea = models.DateTimeField(auto_now_add=True)
    fecha_modificacion_tarea = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo_tarea
