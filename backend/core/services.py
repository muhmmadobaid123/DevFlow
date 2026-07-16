from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task
from bugs.models import Bug


class DashboardFacade:

    @staticmethod
    def get_dashboard():

        return {

            "projects":
            Project.objects.count(),

            "sprints":
            Sprint.objects.count(),

            "tasks":
            Task.objects.count(),

            "bugs":
            Bug.objects.count()
        }