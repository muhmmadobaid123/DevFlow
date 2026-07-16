from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from .models import (
    Notification
)


class NotificationListView(
    APIView
):

    def get(
        self,
        request
    ):

        notifications = (
            Notification.objects()
        )

        result = []

        for item in notifications:

            result.append({

                "id":
                str(item.id),

                "user_id":
                item.user_id,

                "title":
                item.title,

                "message":
                item.message,

                "is_read":
                item.is_read
            })

        return Response(
            result
        )


class MarkAsReadView(
    APIView
):

    def put(
        self,
        request,
        id
    ):

        notification = (
            Notification.objects(
                id=id
            ).first()
        )

        if not notification:

            return Response(
                {
                    "error":
                    "Notification Not Found"
                },
                status=404
            )

        notification.is_read = True

        notification.save()

        return Response(
            {
                "message":
                "Notification Marked As Read"
            }
        )