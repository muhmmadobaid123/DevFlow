from rest_framework.views import APIView
from rest_framework.response import Response
from core.permissions import IsQA
from .models import Bug
from .services import BugService

class CreateBugView(APIView):
    def post(self, request):
        bug = BugService.create_bug(request.data)
        return Response({
            "message": "Bug Created",
            "id": str(bug.id)
        }, status=201)

class GetBugsView(APIView):
    def get(self, request):
        bugs = Bug.objects()
        result = []
        for bug in bugs:
            result.append({
                "id": str(bug.id),
                "task_id": bug.task_id,
                "title": bug.title,
                "description": bug.description,
                "reported_by": bug.reported_by,
                "assigned_to": bug.assigned_to,
                "severity": bug.severity,
                "status": bug.status,
                "created_at": bug.created_at.isoformat() if bug.created_at else None
            })
        return Response(result)

class GetBugView(APIView):
    def get(self, request, id):
        bug = Bug.objects(id=id).first()
        if not bug:
            return Response({"error": "Bug Not Found"}, status=404)
        return Response({
            "id": str(bug.id),
            "task_id": bug.task_id,
            "title": bug.title,
            "description": bug.description,
            "reported_by": bug.reported_by,
            "assigned_to": bug.assigned_to,
            "severity": bug.severity,
            "status": bug.status,
            "created_at": bug.created_at.isoformat() if bug.created_at else None
        })

class AssignBugView(APIView):
    def put(self, request, id):
        bug = Bug.objects(id=id).first()
        if not bug:
            return Response({"error": "Bug Not Found"}, status=404)
        bug.assigned_to = request.data.get("assigned_to", bug.assigned_to)
        bug.status = "Assigned"
        bug.save()
        return Response({"message": "Bug Assigned"})

class ResolveBugView(APIView):
    def put(self, request, id):
        bug = Bug.objects(id=id).first()
        if not bug:
            return Response({"error": "Bug Not Found"}, status=404)
        bug.status = "Resolved"
        bug.save()
        return Response({"message": "Bug Resolved"})

class VerifyBugView(APIView):
    permission_classes = [IsQA]

    def put(self, request, id):
        bug = Bug.objects(id=id).first()
        if not bug:
            return Response({"error": "Bug Not Found"}, status=404)
        bug.status = "Verified"
        bug.save()
        return Response({"message": "Bug Verified"})

class DeleteBugView(APIView):
    def delete(self, request, id):
        bug = Bug.objects(id=id).first()
        if bug:
            bug.delete()
        return Response({"message": "Bug Deleted"})