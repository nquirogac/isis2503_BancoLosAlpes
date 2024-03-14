# This module is responsible for consuming the messages from the broker
import json
import pika
from sys import path
from os import environ


#Define the connection parameters to the broker message
rabbit_host = 'host'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'monitoring_measurements'
topics = ['solicitud_credito']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

for topic in topics:
    channel.queue_bind(
        exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting measurements. To exit press CTRL+C')


def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8').replace("'", '"'))
#    create_measurement_object(
#        variable, payload['value'], payload['unit'], topic[0] + topic[1])
    print("Measurement :%r" % (str(payload)))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()