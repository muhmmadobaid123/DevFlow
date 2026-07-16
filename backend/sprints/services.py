from .models import Sprint


class SprintService:

    @staticmethod
    def create_sprint(data):

        sprint = Sprint(

            project_id=data["project_id"],

            name=data["name"],

            goal=data["goal"],

            start_date=data["start_date"],

            end_date=data["end_date"]

        )

        sprint.save()

        return sprint

    @staticmethod
    def get_sprint(id):

        return Sprint.objects(
            id=id
        ).first()

    @staticmethod
    def get_all_sprints():

        return Sprint.objects()

    @staticmethod
    def delete_sprint(id):

        sprint = Sprint.objects(
            id=id
        ).first()

        if sprint:
            sprint.delete()

        return True