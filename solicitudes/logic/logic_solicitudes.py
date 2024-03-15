from solicitudes.models import Solicitud
def get_solicitudes():
    queryset = Solicitud.objects.all().order_by('status')
    return (queryset)

def create_solicitud(formSolicitud):
    solicitud = formSolicitud.save()
    solicitud.save()

def create_solicitud_object(creationDate, closeDate, status):
    solicitud = Solicitud()
    solicitud.creationDate = creationDate
    solicitud.closeDate = closeDate
    solicitud.status = status
    solicitud.save()
        