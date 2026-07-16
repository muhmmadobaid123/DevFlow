from .models import Task


class TaskService:

    @staticmethod
    def create_task(data):

        task = Task(

            sprint_id=data["sprint_id"],

            title=data["title"],

            description=data["description"],

            assigned_to=data["assigned_to"],

            priority=data["priority"]

        )

        task.save()

        return task

    @staticmethod
    def get_all():

        return Task.objects()

    @staticmethod
    def get(id):

        return Task.objects(
            id=id
        ).first()