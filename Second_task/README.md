# Домашнє завдання. Частина друга

Цей проєкт реалізує імітацію обробки контактів і відправки повідомлень з використанням RabbitMQ та Python.

## Огляд

Проєкт складається з двох основних частин: генерація фейкових контактів та обробка їх для відправки повідомлень.

1. **Генерація фейкових контактів**: У файлі `producer.py` використовується бібліотека Faker для генерації фейкових контактів. Кожен контакт має ім'я, адресу, електронну пошту, номер телефону.

2. **Обробка контактів і відправка електронних листів**: У файлі `producer.py` контакти відправляються на обробку через RabbitMQ. 

3. **Обробка повідомлень**: У файлі `consumer.py` обробляються повідомлення.


## Вимоги

Перед використанням проекту переконайтеся, що у вас встановлені наступні залежності:

- Python (рекомендована версія 3.6+)
- Бібліотеки, перераховані в `requirements.txt`
- Docker

## Запуск RabbitMQ в Docker

Для запуску RabbitMQ в Docker, використовуйте наступну команду:

docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

Ця команда завантажує та запускає офіційний Docker-контейнер RabbitMQ з веб-інтерфейсом на портах 5672 (AMQP) і 15672 (керування).

## Встановлення та запуск
1. Клонуйте репозиторій

2. Встановіть залежності:

pip install -r requirements.txt

3. Запустіть обробку контактів та відправку SMS і електронних листів:

python producer.py

4. У окремих терміналах запустіть обробку повідомлень:

python consumer.py

## Конфігурація
Для налаштування підключення до MongoDB, редагуйте відповідні змінні у файлі config.ini.

## Автор
Устименко Оксана Борисівна

## Ліцензія
Цей проєкт розповсюджується під ліцензією MIT License.
