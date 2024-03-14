#!/usr/bin/env python
import time
import pika
import json

from random import choice, randint
from datetime import datetime
from os import environ
from config.config import RABBIT_HOST, RABBIT_USER, RABBIT_PASSWORD

rabbit_host = RABBIT_HOST
rabbit_user = RABBIT_USER
rabbit_password = RABBIT_PASSWORD
exchange = 'BancoLosAlpes_solicitudes_credito'
topic = 'solicitud_credito'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Sending solicitude. To exit press CTRL+C')

while True:
    operation = choice(['creacion', 'modificacion', 'eliminacion'])
    userId = randint(10000, 99999)
    timestamp = datetime.now().isoformat() 
    payload = {'operation': operation, 'userId': userId, 'timestamp': timestamp} # JSON
    message_body = json.dumps(payload)  # Convertir el diccionario a JSON
    channel.basic_publish(exchange=exchange,
                          routing_key=topic, body=message_body)
    print("Request: %r by: %r at: %s" % (operation, userId, timestamp))
    time.sleep(8)

connection.close()