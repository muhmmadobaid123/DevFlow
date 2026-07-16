from mongoengine import *

class Project(Document):

    name = StringField(required=True)

    description = StringField()

    status = StringField()

    manager_id = StringField()

    meta = {
        "collection": "projects"
    }