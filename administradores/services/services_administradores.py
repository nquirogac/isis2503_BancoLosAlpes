from ..logic.logic_administradores import getAdministradorByDocumento

def getAdministrador(documento):
    rtaAdministrador = None
    administrador = getAdministradorByDocumento(documento)
    if administrador != None:
        rtaAdministrador = administrador
    else:
        rtaAdministrador = 'No hay administrador con ese documento'
    return rtaAdministrador

