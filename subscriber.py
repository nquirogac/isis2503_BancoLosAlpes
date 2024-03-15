import json
from random import randint
import pika
from sys import path
from os import environ
import django
from pymongo import MongoClient, errors

# Configuraciones de conexión a MongoDB
MONGO_CONN_STRING = 'mongodb+srv://TomasR:20220722@prueba1.00rxmli.mongodb.net/'
MONGO_DB_NAME = 'AWS'
MONGO_COLLECTION_NAME = 'solicitudesLogs'

try:
    client = MongoClient(MONGO_CONN_STRING)
    db = client[MONGO_DB_NAME]
    collection = db[MONGO_COLLECTION_NAME]
    print("> Conexión a MongoDB exitosa")
except errors.ConnectionFailure as e:
    print(f"> Error de conexión a MongoDB: {e}")
    exit()

# Configuraciones de conexión a RabbitMQ
RABBIT_HOST = '10.128.0.5'
RABBIT_USER = 'monitoring_user'
RABBIT_PASSWORD = 'isis2503'
EXCHANGE = 'BancoLosAlpes'
TOPICS = ['solicitud']

# Configuración de Django
path.append('isis2503_BancoLosAlpes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'isis2503_BancoLosAlpes.settings')
django.setup()

# Importaciones de Django (ubicarlas aquí para evitar errores de configuración no inicializada)
from solicitudes.logic.logic_solicitudes import createSolicitudObject
from clientes.services.services_clientes import getCliente

# Establecer conexión con RabbitMQ
connection_params = pika.ConnectionParameters(
    host=RABBIT_HOST,
    credentials=pika.PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
)

try:
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE, exchange_type='topic')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    for topic in TOPICS:
        channel.queue_bind(exchange=EXCHANGE, queue=queue_name, routing_key=topic)
    print('> Esperando logs. Para salir presione CTRL+C')
except pika.exceptions.AMQPError as e:
    print(f"> Error conectando con RabbitMQ: {e}")
    exit()

def callback(ch, method, properties, body):
    try:
        payload = json.loads(body.decode('utf8').replace("'", '"'))
        print('Fecha de Creación: ' + str(payload['creationDate']) +
              ', Estado: ' + str(payload['status']) + ', Documento Cliente: ' + str(payload['user_id']))
        id = randint(-9223372036854775807, 9223372036854775807)
        log = {
            '_id': id,
            "user_id": payload['user_id'],
            "creationDate": payload['creationDate'],
            "status": payload['status']
        }
        collection.insert_one(log)
    except Exception as e:
        print(f"> Error procesando mensaje: {e}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("> Proceso interrumpido por el usuario")
except Exception as e:
    print(f"> Error durante la consumición de mensajes: {e}")
finally:
    connection.close()
    print("> Conexión con RabbitMQ cerrada")
