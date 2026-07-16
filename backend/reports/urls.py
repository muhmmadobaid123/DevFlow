from django.urls import path

from .views import (
    GenerateReportView
)

from .dashboard import (
    DashboardView
)

urlpatterns = [

    path(
        "generate/",
        GenerateReportView.as_view()
    ),

    path(
        "dashboard/",
        DashboardView.as_view()
    )
]