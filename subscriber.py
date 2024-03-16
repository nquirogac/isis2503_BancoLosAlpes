import json
from random import randint
import pika
from sys import path
from os import environ
import django

#Define the connection parameters to the broker message
rabbit_host = '10.128.0.5'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'BancoLosAlpes'
topics = ['solicitud']

path.append('isis2503_BancoLosAlpes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'isis2503_BancoLosAlpes.settings')
django.setup()

from solicitudes.logic.logic_solicitudes import createSolicitudObject
from clientes.services.services_clientes import getCliente
from logs.models import Log  # replace 'logs' with your Django app name

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


def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
    createSolicitudObject(payload['creationDate'], payload['status'], payload['user_id'])
    print('Creation Date ' + str(payload['creationDate']) + 
          + 'Status ' + str(payload['status']) + 'Docuemnto Cliente ' + str(payload['user_id']))
    Log.objects.using('logs').create(level='INFO', message=f"Creation Date {str(payload['creationDate'])} Status {str(payload['status'])} Docuemnto Cliente {str(payload['user_id'])}")  

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()