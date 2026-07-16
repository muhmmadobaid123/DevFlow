from rest_framework.views import APIView
from rest_framework.response import Response
from core.permissions import IsDeveloper
from .models import Task
from .services import TaskService

class CreateTaskView(APIView):
    def post(self, request):
        task = TaskService.create_task(request.data)
        return Response({
            "message": "Task Created",
            "id": str(task.id)
        }, status=201)

class GetTasksView(APIView):
    def get(self, request):
        tasks = TaskService.get_all()
        result = []
        for task in tasks:
            result.append({
                "id": str(task.id),
                "sprint_id": task.sprint_id,
                "title": task.title,
                "description": task.description,
                "assigned_to": task.assigned_to,
                "priority": task.priority,
                "status": task.status,
                "created_at": task.created_at.isoformat() if task.created_at else None
            })
        return Response(result)

class GetTaskView(APIView):
    def get(self, request, id):
        task = TaskService.get(id)
        if not task:
            return Response({"error": "Task Not Found"}, status=404)
        return Response({
            "id": str(task.id),
            "sprint_id": task.sprint_id,
            "title": task.title,
            "description": task.description,
            "assigned_to": task.assigned_to,
            "priority": task.priority,
            "status": task.status,
            "created_at": task.created_at.isoformat() if task.created_at else None
        })

class UpdateTaskView(APIView):
    def put(self, request, id):
        task = Task.objects(id=id).first()
        if not task:
            return Response({"error": "Task Not Found"}, status=404)
        task.sprint_id = request.data.get("sprint_id", task.sprint_id)
        task.title = request.data.get("title", task.title)
        task.description = request.data.get("description", task.description)
        task.assigned_to = request.data.get("assigned_to", task.assigned_to)
        task.priority = request.data.get("priority", task.priority)
        task.status = request.data.get("status", task.status)
        task.save()
        return Response({"message": "Task Updated"})

class DeleteTaskView(APIView):
    def delete(self, request, id):
        task = Task.objects(id=id).first()
        if task:
            task.delete()
        return Response({"message": "Task Deleted"})

class ChangeTaskStatusView(APIView):
    permission_classes = [IsDeveloper]

    def put(self, request, id):
        task = Task.objects(id=id).first()
        if not task:
            return Response({"error": "Task Not Found"}, status=404)
        
        from .state import TodoState, InProgressState, TestingState, DoneState
        state_map = {
            "Todo": TodoState(),
            "InProgress": InProgressState(),
            "Testing": TestingState(),
            "Done": DoneState()
        }
        current_state_str = task.status or "Todo"
        state_inst = state_map.get(current_state_str, TodoState())
        next_state = state_inst.next()
        task.status = next_state
        task.save()
        
        return Response({
            "message": "Task Status Changed",
            "status": task.status
        })