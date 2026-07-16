from mongoengine import *
from datetime import datetime


class ActivityLog(Document):

    user_id = StringField()

    action = StringField()

    module = StringField()

    created_at = DateTimeField(
        default=datetime.utcnow
    )

    meta = {
        "collection": "logs"
    }