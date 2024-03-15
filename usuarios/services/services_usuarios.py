from ..logic.logic_usuarios import getUsuarioByDocument

def getUsuario(document):
    rtaUser = None
    user = getUsuarioByDocument(document)
    if user != None:
        rtaUser = user
    else:
        rtaUser = 'No hay usuario con ese documento'
    return rtaUser