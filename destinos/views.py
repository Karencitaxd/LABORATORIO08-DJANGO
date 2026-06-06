from django.shortcuts import render, redirect, get_object_or_404
from .models import DestinoTuristico
from .forms import DestinoForm


def index(request):
    destinos = DestinoTuristico.objects.all()

    return render(request, 'destinos/index.html', {
        'destinos': destinos
    })


def agregar_destino(request):

    if request.method == 'POST':
        formulario = DestinoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('index')

    else:
        formulario = DestinoForm()

    return render(
        request,
        'destinos/agregar_destino.html',
        {'formulario': formulario}
    )


def editar_destino(request, id):

    destino = get_object_or_404(
        DestinoTuristico,
        id=id
    )

    if request.method == 'POST':

        formulario = DestinoForm(
            request.POST,
            request.FILES,
            instance=destino
        )

        if formulario.is_valid():
            formulario.save()
            return redirect('index')

    else:

        formulario = DestinoForm(
            instance=destino
        )

    return render(
        request,
        'destinos/editar_destino.html',
        {'formulario': formulario}
    )