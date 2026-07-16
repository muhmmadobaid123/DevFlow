from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sprint
from .services import SprintService


class CreateSprintView(APIView):

    def post(self, request):

        sprint = SprintService.create_sprint(
            request.data
        )

        return Response({

            "message":
            "Sprint Created",

            "id":
            str(sprint.id)

        })


class GetSprintsView(APIView):

    def get(self, request):

        sprints = Sprint.objects()

        result = []

        for sprint in sprints:

            result.append({

                "id":
                str(sprint.id),

                "project_id":
                sprint.project_id,

                "name":
                sprint.name,

                "goal":
                sprint.goal,

                "status":
                sprint.status

            })

        return Response(result)


class GetSprintView(APIView):

    def get(self, request, id):

        sprint = Sprint.objects(
            id=id
        ).first()

        if not sprint:

            return Response(
                {
                    "error":
                    "Sprint Not Found"
                },
                status=404
            )

        return Response({

            "id":
            str(sprint.id),

            "project_id":
            sprint.project_id,

            "name":
            sprint.name,

            "goal":
            sprint.goal,

            "status":
            sprint.status

        })


class UpdateSprintView(APIView):

    def put(self, request, id):

        sprint = Sprint.objects(
            id=id
        ).first()

        if not sprint:

            return Response(
                {
                    "error":
                    "Sprint Not Found"
                },
                status=404
            )

        sprint.name = request.data["name"]

        sprint.goal = request.data["goal"]

        sprint.status = request.data["status"]

        sprint.save()

        return Response({

            "message":
            "Sprint Updated"

        })


class DeleteSprintView(APIView):

    def delete(self, request, id):

        sprint = Sprint.objects(
            id=id
        ).first()

        if sprint:
            sprint.delete()

        return Response({

            "message":
            "Sprint Deleted"

        })


class CloseSprintView(APIView):

    def put(self, request, id):

        sprint = Sprint.objects(
            id=id
        ).first()

        if not sprint:

            return Response(
                {
                    "error":
                    "Sprint Not Found"
                },
                status=404
            )

        sprint.status = "Completed"

        sprint.save()

        return Response({

            "message":
            "Sprint Closed"

        })