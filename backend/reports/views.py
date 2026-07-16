from rest_framework.views import APIView
from rest_framework.response import Response

from .services import (
    ReportService
)


class GenerateReportView(
    APIView
):

    def get(
        self,
        request
    ):

        report = (
            ReportService
            .generate_report()
        )

        return Response(
            report
        )