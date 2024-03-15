from ..logic.logic_clientes import getClienteByDocumento

def getCliente(documento):
    rtaCliente = None
    cliente = getClienteByDocumento(documento)
    if cliente != None:
        rtaCliente = cliente
    else:
        rtaCliente = 'No hay cliente con ese documento'
    return rtaCliente