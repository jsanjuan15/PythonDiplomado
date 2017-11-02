from django.conf.urls import url

from . import views

app_name = 'tareas'
urlpatterns = [
    url(r'^(?P<l_id>[0-9]+)/$', views.listaTareas, name='listado_tareas'),
    url(r'^(?P<l_id>[0-9]+)/pendiente_tarea$', views.DesmarcarTarea, name='pendiente_tarea'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^crear_lista/$', views.ListaCreateView.as_view(), name='crear_lista'),
    url(r'^(?P<pk>[0-9]+)/modificar_lista$', views.ListaUpdateView.as_view(), name='modificar_lista'),
    url(r'^(?P<pk>[0-9]+)/eliminar_lista$', views.ListaDelete.as_view(), name='eliminar_lista'),
    url(r'^crear_tarea/$', views.TareasCreateView.as_view(), name='crear_tarea'),
    url(r'^(?P<pk>[0-9]+)/modificar_tarea$', views.TareasUpdateView.as_view(), name='modificar_tarea'),
    url(r'^(?P<pk>[0-9]+)/eliminar_tarea$', views.TareasDelete.as_view(), name='eliminar_tarea'),
    url(r'^pendientes/$', views.TareasPendientesView.as_view(), name='pendientes'),
    url(r'^terminadas/$', views.TareasTerminadasMesView.as_view(), name='terminadas'),
    url(r'^pendientes_mes/$', views.TareasPendientesMesView.as_view(), name='pendientes_mes'),
]
