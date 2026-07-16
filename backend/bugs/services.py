from .models import Bug


class BugService:

    @staticmethod
    def create_bug(data):

        bug = Bug(

            task_id=data["task_id"],

            title=data["title"],

            description=data["description"],

            reported_by=data[
                "reported_by"
            ],

            assigned_to=data[
                "assigned_to"
            ],

            severity=data["severity"]

        )

        bug.save()

        return bug