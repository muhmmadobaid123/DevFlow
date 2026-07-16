from mongoengine import *
from datetime import datetime


class User(Document):

    name = StringField(required=True)

    email = EmailField(
        required=True,
        unique=True
    )

    password = StringField(
        required=True
    )

    role = StringField(
        choices=[
            "Admin",
            "ProjectManager",
            "Developer",
            "QA",
            "Client"
        ]
    )

    created_at = DateTimeField(
        default=datetime.utcnow
    )