import faker
from random import randint, choice

import pika

import connect
from models import Contact

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='send_message', exchange_type='topic')

channel.queue_declare(queue='sms_queue', durable=True)
channel.queue_declare(queue='email_queue', durable=True)
channel.queue_bind(exchange='send_message',
                   queue='sms_queue', routing_key='sms')
channel.queue_bind(exchange='send_message',
                   queue='email_queue', routing_key='email')


def main():
    fake_data = faker.Faker()
    for _ in range(2):
        fake_name = fake_data.name()
        fake_address = fake_data.address()
        fake_email = fake_data.email()
        fake_phone_number = '+380' + str(randint(111111111, 999999999))
        fake_sms = choice([True, False])

        contact = Contact(fullname=fake_name, 
                          address=fake_address,
                          email=fake_email,
                          phone=fake_phone_number,
                          sms = fake_sms).save()
        

        routing_key = 'sms' if contact.sms else 'email'

        channel.basic_publish(
            exchange='send_message',
            routing_key=routing_key,
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(f" [x] Send message to {contact.fullname}")
    connection.close()


if __name__ == '__main__':
    main()
