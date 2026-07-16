from projects.models import Project
from sprints.models import Sprint
from tasks.models import Task
from bugs.models import Bug

from .builder import (
    ReportBuilder
)


class ReportService:

    @staticmethod
    def generate_report():

        builder = ReportBuilder()

        builder.project_count(
            Project.objects.count()
        )

        builder.sprint_count(
            Sprint.objects.count()
        )

        builder.task_count(
            Task.objects.count()
        )

        builder.bug_count(
            Bug.objects.count()
        )

        return builder.get_report()