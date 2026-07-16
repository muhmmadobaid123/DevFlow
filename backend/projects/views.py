from rest_framework.views import APIView
from rest_framework.response import Response
from core.permissions import IsProjectManager
from .models import Project
from .services import ProjectService

class CreateProjectView(APIView):
    permission_classes = [IsProjectManager]

    def post(self, request):
        project = ProjectService.create_project(request.data)
        return Response({
            "message": "Project Created",
            "id": str(project.id)
        }, status=201)

class GetProjectsView(APIView):
    def get(self, request):
        projects = ProjectService.get_all_projects()
        result = []
        for project in projects:
            result.append({
                "id": str(project.id),
                "name": project.name,
                "description": project.description,
                "status": project.status,
                "manager_id": getattr(project, "manager_id", None)
            })
        return Response(result)

class GetProjectView(APIView):
    def get(self, request, id):
        project = ProjectService.get_project(id)
        if not project:
            return Response({"error": "Project Not Found"}, status=404)
        return Response({
            "id": str(project.id),
            "name": project.name,
            "description": project.description,
            "status": project.status,
            "manager_id": getattr(project, "manager_id", None)
        })

class UpdateProjectView(APIView):
    def put(self, request, id):
        project = ProjectService.get_project(id)
        if not project:
            return Response({"error": "Project Not Found"}, status=404)
        project.name = request.data.get("name", project.name)
        project.description = request.data.get("description", project.description)
        project.status = request.data.get("status", project.status)
        project.manager_id = request.data.get("manager_id", project.manager_id)
        project.save()
        return Response({"message": "Project Updated"})

class DeleteProjectView(APIView):
    def delete(self, request, id):
        ProjectService.delete_project(id)
        return Response({"message": "Project Deleted"})