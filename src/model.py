from mongoengine import Document
from mongoengine import StringField, ListField


class Page(Document):
    meta = {'collection': 'pages'}
    title = StringField()
    date = StringField()
    content = StringField()
    tags = ListField(StringField())
