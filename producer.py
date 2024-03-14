#!/usr/bin/env python
import time
import pika
from random import choice

rabbit_host = 'host'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
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