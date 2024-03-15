from django.shortcuts import render
from django.contrib import messages
from .forms import usuarioForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_usuarios import getUsuarios, createUsuario

def usuariosList(request):
    listaUser = getUsuarios()
    context = {
        'usuariosList': listaUser
    }
    return render(request, 'usuariosList/usuarios.html', context)

def postUsuario(request):
    if request.method == 'POST':
        form = usuarioForm(request.POST)
        if form.is_valid():
            createUsuario(form)
            messages.add_message(request, messages.SUCCESS, 'Usuario created successful')
            return HttpResponseRedirect(reverse('createUsuario'))
        else:
            print(form.errors)
    else:
        form = usuarioForm()

    context = {
        'form': form,
    }

    return render(request, 'usuarios/createUsuarios.html', context)
            