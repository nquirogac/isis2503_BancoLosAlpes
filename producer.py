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
exchange = 'BancoLosAlpes'
topics = ['solicitud', 'cliente', 'producto']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Sending solicitude. To exit press CTRL+C')

while True:
    for topic in topics:
        operation = choice(['creacion', 'modificacion', 'eliminacion'])
        status = choice(['pendiente', 'aprobada', 'rechazada'])
        userId = randint(10000, 99999)
        timestamp = datetime.now().isoformat() 
        payload = {'Topic': topic, 'operation': operation, 'status': status, 'userId': userId, 'timestamp': timestamp} # JSON
        message_body = json.dumps(payload)  # Convertir el diccionario a JSON
        channel.basic_publish(exchange=exchange,
                            routing_key=topic, body=message_body)
        print("Topic: %r Request: %r Staus: %r by: %r at: %s" % (topic,operation,status, userId, timestamp))
        time.sleep(1)

connection.close()