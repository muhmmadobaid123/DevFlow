from .models import Project


class ProjectService:

    @staticmethod
    def create_project(data):

        project = Project(
            name=data["name"],
            description=data["description"],
            manager_id=data["manager_id"]
        )

        project.save()

        return project

    @staticmethod
    def get_all_projects():

        return Project.objects()

    @staticmethod
    def get_project(project_id):

        return Project.objects(
            id=project_id
        ).first()

    @staticmethod
    def delete_project(project_id):

        project = Project.objects(
            id=project_id
        ).first()

        if project:
            project.delete()

        return True