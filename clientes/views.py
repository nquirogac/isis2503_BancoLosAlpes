from django.shortcuts import render
from django.contrib import messages
from .forms import clienteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from clientes.logic.logic_clientes import getClientes, createCliente

def clientesList(request):
    listaClientes = getClientes()
    context = {
        'clientesList': listaClientes
    }
    return render(request, 'clientesList/clientes.html', context)

def postCliente(request):
    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            createCliente(form)
            messages.add_message(request, messages.SUCCESS, 'Cliente created successful')
            return HttpResponseRedirect(reverse('createCliente'))
        else:
            print(form.errors)
    else:
        form = clienteForm()

    context = {
        'form': form,
    }

    return render(request, 'clientes/createClientes.html', context)



