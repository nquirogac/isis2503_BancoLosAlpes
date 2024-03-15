from clientes.models import Cliente
from usuarios.logic.logic_usuarios import getUsuarios, createUsuario, createUsuarioObject, getUsuarioByDocument


def getClientes():
    queryset = Cliente.objects.all().order_by('document')
    return(queryset)

def createCliente(formCliente):
    user = formCliente.save()
    user.save()

def createClienteObject(name, lastName, document, age, email, country, city, income, debt, economicActivity, company, profession):
    user = Cliente()
    user.name = name
    user.lastName = lastName
    user.document = document
    user.age = age
    user.email = email
    user.country = country
    user.city = city
    user.income = income
    user.debt = debt
    user.economicActivity = economicActivity
    user.company = company
    user.profession = profession
    user.save()
    
def getClienteByDocumento(document):
    userSelect = None
    try:
        user = Cliente.objects.get(document=document)
        userSelect = user
    except:
        userSelect
    return userSelect
    
    
