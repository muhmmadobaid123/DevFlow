from mongoengine import *
from datetime import datetime


class Bug(Document):

    task_id = StringField(
        required=True
    )

    title = StringField(
        required=True
    )

    description = StringField()

    reported_by = StringField()

    assigned_to = StringField()

    severity = StringField(
        choices=[
            "Low",
            "Medium",
            "High",
            "Critical"
        ],
        default="Low"
    )

    status = StringField(
        choices=[
            "Open",
            "Assigned",
            "Resolved",
            "Verified",
            "Closed"
        ],
        default="Open"
    )

    created_at = DateTimeField(
        default=datetime.utcnow
    )

    meta = {
        "collection": "bugs"
    }