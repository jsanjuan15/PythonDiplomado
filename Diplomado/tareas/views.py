from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Lista, Tareas
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ListaForm, TareasForm
from django.utils import timezone
import datetime
from django.contrib import messages

def listaTareas(request, l_id):
    try:
        lista = Lista.objects.get(pk=l_id)
    except lista.DoesNotExist:
        raise Http404("La Lista No existe")
    return render(request, 'tareas/listado_tareas.html', {'lista': lista})

def DesmarcarTarea(request, l_id):
    try:
        fecha = timezone.now() - datetime.timedelta(days=30)
        tarea = Tareas.objects.get(pk=l_id)
    except tarea.DoesNotExist:
        raise Http404("La Tarea no exite")
    else:
        if tarea.fecha_creacion_tarea < fecha and tarea.estado_tarea == True:
            messages.add_message(request, messages.ERROR, 'La tarea Tiene mas de 30 dias de CREADA y esta TERMINADA.')
            return HttpResponseRedirect(reverse('tareas:listado_tareas', kwargs={'l_id': tarea.id_lista_id}))
        else:
            if tarea.estado_tarea == True:
                tarea.estado_tarea = False
                tarea.save()
                messages.add_message(request, messages.ERROR, 'Tarea Marcada como Pendiente.')
            else:
                tarea.estado_tarea = True
                tarea.save()
                messages.add_message(request, messages.SUCCESS, 'Tarea Marcada como Terminada.')
            return HttpResponseRedirect(reverse('tareas:listado_tareas', kwargs={'l_id': tarea.id_lista_id}))


class IndexView(generic.ListView):
    template_name = 'tareas/index.html'
    context_object_name = 'listado'

    def get_queryset(self):
        """Return the last five published questions."""
        return Lista.objects.all()


class ListaCreateView(SuccessMessageMixin, generic.CreateView):
    model = Lista
    form_class = ListaForm
    success_url = reverse_lazy('tareas:index')
    success_message = "Lista Creada Con Exito"

class ListaUpdateView(generic.UpdateView):
    model = Lista
    form_class = ListaForm
    success_url = reverse_lazy('tareas:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.titulo_lista = self.object.titulo_lista
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Lista Modificada con exito.')
        return HttpResponseRedirect(self.get_success_url())


class ListaDelete(generic.DeleteView):
    model = Lista
    success_url = reverse_lazy('tareas:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        messages.add_message(self.request, messages.SUCCESS, 'Lista Eliminada con exito.')
        return HttpResponseRedirect(self.get_success_url())


class TareasCreateView(SuccessMessageMixin, generic.CreateView):
    model = Tareas
    form_class = TareasForm
    success_url = reverse_lazy('tareas:index')
    success_message = "Tarea Creada Con Exito"


class TareasUpdateView(generic.UpdateView):
    model = Tareas
    form_class = TareasForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        print("kwargs = %s" % self.kwargs)
        self.object.titulo_tarea = self.object.titulo_tarea
        self.object.estado_tarea = self.object.estado_tarea
        self.object.id_lista = self.object.id_lista
        self.object.descripcion_tarea = self.object.descripcion_tarea
        self.object.save()
        messages.add_message(self.request, messages.SUCCESS, 'Tarea Modificada con exito.')
        return HttpResponseRedirect(reverse('tareas:listado_tareas', kwargs={'l_id': self.object.id_lista_id}))
   

class TareasDelete (generic.DeleteView):
    model = Tareas

    def delete(self, request, *args, **kwargs):
        id_lis = self.get_object().id_lista_id
        self.object = self.get_object()
        self.object.delete()
        messages.add_message(self.request, messages.SUCCESS, 'Tarea Eliminada con exito.')
        return HttpResponseRedirect(reverse('tareas:listado_tareas', kwargs={'l_id': id_lis}))
    

class TareasPendientesView(generic.ListView):
    template_name = 'tareas/reportes.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Tareas.objects.filter(estado_tarea="False")


class TareasTerminadasMesView(generic.ListView):
    template_name = 'tareas/reportes.html'
    context_object_name = 'lista'

    def get_queryset(self):
        return Tareas.objects.filter(estado_tarea="True", fecha_modificacion_tarea__month=timezone.now().month)


class TareasPendientesMesView(generic.ListView):
    template_name = 'tareas/reportes.html'
    context_object_name = 'lista'

    def get_queryset(self):
        fecha = timezone.now() - datetime.timedelta(days=30)
        return Tareas.objects.filter(estado_tarea="False", fecha_creacion_tarea__lt=fecha)