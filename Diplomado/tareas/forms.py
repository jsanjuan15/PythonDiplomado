from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = "date"


class ListaForm(forms.ModelForm):
    titulo_lista = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = models.Lista
        fields = ['titulo_lista']


class TareasForm(forms.ModelForm):
    titulo_tarea = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    descripcion_tarea = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
   

    class Meta:
        model = models.Tareas
        fields = ['id_lista','titulo_tarea','descripcion_tarea']
