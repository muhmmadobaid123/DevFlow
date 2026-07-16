from mongoengine import *
from datetime import datetime


class Task(Document):

    sprint_id = StringField(
        required=True
    )

    title = StringField(
        required=True
    )

    description = StringField()

    assigned_to = StringField()

    priority = StringField(
        choices=[
            "Low",
            "Medium",
            "High"
        ],
        default="Medium"
    )

    status = StringField(
        choices=[
            "Todo",
            "InProgress",
            "Testing",
            "Done"
        ],
        default="Todo"
    )

    created_at = DateTimeField(
        default=datetime.utcnow
    )

    meta = {
        "collection": "tasks"
    }