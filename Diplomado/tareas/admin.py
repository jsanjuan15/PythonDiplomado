from django.contrib import admin

from .models import Lista, Tareas

class ListaAdmin(admin.ModelAdmin):
    list_display = ["titulo_lista", "fecha_lista"]
    search_fields = ["titulo_lista"]

class TareasAdmin(admin.ModelAdmin):
    list_display = ["titulo_tarea", "estado_tarea", "fecha_creacion_tarea", "fecha_modificacion_tarea", "descripcion_tarea"]
    search_fields = ["titulo_tarea"]

admin.site.register(Lista, ListaAdmin)
admin.site.register(Tareas, TareasAdmin)
