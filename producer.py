#!/usr/bin/env python
import time
import pika
from random import choice, randint
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
    payload = {'operation': operation, 'userId': userId} # JSON
    channel.basic_publish(exchange=exchange,
                          routing_key=topic, body=payload)
    print("Request: %r by: %r" % (operation, userId))
    time.sleep(8)

connection.close()