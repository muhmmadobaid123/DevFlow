from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from core.permissions import (
    IsAdmin
)

from accounts.models import User


class UsersListView(APIView):

    permission_classes = [
        IsAdmin
    ]

    def get(self, request):

        users = User.objects()

        result = []

        for user in users:

            result.append({

                "id":
                str(user.id),

                "name":
                user.name,

                "email":
                user.email,

                "role":
                user.role
            })

        return Response(
            result
        )