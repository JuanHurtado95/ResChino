from django.shortcuts import render, redirect
from .forms import ingredientesForm
from .models import ingredientes
from django.db.models import Q
# Create your views here.

def Menu(request):
    return render(request, 'menu.html')


def show(request):
    queryset = request.GET.get("buscar")
    asignatura = ingredientes.objects.all() 
    if queryset:
        asignatura = ingredientes.objects.filter(
            Q(nombre__icontains=queryset)
        )
    return render(request, "menu.html", {'asignaturas' : asignatura})