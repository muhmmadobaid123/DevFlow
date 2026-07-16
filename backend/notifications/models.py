from mongoengine import *
from datetime import datetime


class Notification(Document):

    user_id = StringField()

    title = StringField()

    message = StringField()

    is_read = BooleanField(
        default=False
    )

    created_at = DateTimeField(
        default=datetime.utcnow
    )