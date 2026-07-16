from mongoengine import *
from datetime import datetime


class Sprint(Document):

    project_id = StringField(
        required=True
    )

    name = StringField(
        required=True
    )

    goal = StringField()

    start_date = DateTimeField()

    end_date = DateTimeField()

    status = StringField(
        default="Planned"
    )

    created_at = DateTimeField(
        default=datetime.utcnow
    )

    meta = {
        "collection": "sprints"
    }