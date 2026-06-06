from django.shortcuts import render
from .models import DestinoTuristico

def index(request):
    destinos = DestinoTuristico.objects.all()

    return render(request, 'destinos/index.html', {
        'destinos': destinos
    })