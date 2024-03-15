from usuarios.models import Usuario
def getUsuarios():
    queryset = Usuario.objects.all().order_by('document')
    return(queryset)

def createUsuario(formUsuario):
    user = formUsuario.save()
    user.save()
    
def createUsuarioObject(name, lastName, document, age, email, country, city):
    user = Usuario()
    user.name = name
    user.lastName = lastName
    user.document = document
    user.age = age
    user.email = email
    user.country = country
    user.city = city
    user.save()
    
def getUsuarioByDocument(document):
    userSelect = None
    try:
        user = Usuario.objects.get(document=document)
        userSelect = user
    except:
        userSelect
    return userSelect

        
    