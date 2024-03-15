import json
import pika
from sys import path
from os import environ
import django


#Define the connection parameters to the broker message
rabbit_host = ''
rabbit_user = ''
rabbit_password = ''
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('isis2503_BancoLosAlpes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'isis2503_BancoLosAlpes.settings')
django.setup()

from solicitudes.logic.logic_solicitudes import createSolicitudObject
from clientes.services.services_clientes import getCliente

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting logs. To exit press CTRL+C')


def callback(body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    if getCliente(payload['user_id']) != 'No hay cliente con ese documento':
        createSolicitudObject(payload['creationDate'], payload['closeDate'], payload['status'], payload['user_id'])
        print('Creation Date ' + str(payload['creationDate']) + ' Close Date ' + str(payload['closeDate']) 
              + 'Status ' + str(payload['status']) + 'Docuemnto Cliente ' + str(payload['user_id']))
    else: 
        print('error, el usuario no se encuenta en el CRM')

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()