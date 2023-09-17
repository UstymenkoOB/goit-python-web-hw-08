from mongoengine import Document
from mongoengine.fields import StringField, EmailField, BooleanField


class Contact(Document):
    fullname = StringField(max_length=150)
    address = StringField(max_length=100)
    email = EmailField(max_length=50)
    phone = StringField(max_length=20)
    done = BooleanField(default=False)
    meta = {"collection": 'contacts'}
