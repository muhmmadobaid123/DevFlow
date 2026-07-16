from rest_framework.views import (
    APIView
)

from rest_framework.response import (
    Response
)

from core.services import (
    DashboardFacade
)


class DashboardView(
    APIView
):

    def get(
        self,
        request
    ):

        return Response(

            DashboardFacade
            .get_dashboard()

        )