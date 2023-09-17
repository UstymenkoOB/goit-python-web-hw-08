import pika

import connect
from models import Contact

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='sms_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    pk = body.decode()
    contact = Contact.objects(id=pk, done=False).first()
    if contact:
        contact.update(set__done=True)
        print(f"SMS was sent to {contact.fullname}'s phone number: {contact.phone}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='sms_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()
