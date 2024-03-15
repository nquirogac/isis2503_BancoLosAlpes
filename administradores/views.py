from django.shortcuts import render
from django.contrib import messages
from .forms import administradorForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from administradores.logic.logic_administradores import getAdministradores, createAdministrador

def administradoresList(request):
    listaAdministradores = getAdministradores()
    context = {
        'administradoresList': listaAdministradores
    }
    return render(request, 'administradoresList/administradores.html', context)

def postAdministrador(request):
    if request.method == 'POST':
        form = administradorForm(request.POST)
        if form.is_valid():
            createAdministrador(form)
            messages.add_message(request, messages.SUCCESS, 'Administrador created successful')
            return HttpResponseRedirect(reverse('createAdministrador'))
        else:
            print(form.errors)
    else:
        form = administradorForm()

    context = {
        'form': form,
    }

    return render(request, 'administradores/createAdministradores.html', context)


# Create your views here.
