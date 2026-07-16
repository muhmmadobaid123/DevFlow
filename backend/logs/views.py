from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ActivityLog


class ActivityLogsView(APIView):

    def get(self, request):

        logs = ActivityLog.objects()

        result = []

        for log in logs:

            result.append({

                "user_id":
                log.user_id,

                "action":
                log.action,

                "module":
                log.module

            })

        return Response(result)