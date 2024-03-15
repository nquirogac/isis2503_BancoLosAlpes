from administradores.models import Administrador
from usuarios.logic.logic_usuarios import getUsuarios, createUsuario, createUsuarioObject, getUsuarioByDocument

def getAdministradores():
    queryset = Administrador.objects.all().order_by('login')
    return(queryset)

def createAdministrador(formAdministrador):
    user = formAdministrador.save()
    user.save()

def createAdministratorObject(name, lastName, document, age, email, country, city, login, password):
    user = Administrador()
    user.name = name
    user.lastName = lastName
    user.document = document
    user.age = age
    user.email = email
    user.country = country
    user.city = city
    user.login = login
    user.password = password
    user.save()
    
def getAdministradorByDocumento(document):
    userSelect = None
    try:
        user = Administrador.objects.get(document=document)
        userSelect = user
    except:
        userSelect
    return userSelect