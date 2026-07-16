from django.urls import path

from .views import (

    CreateProjectView,

    GetProjectsView,

    GetProjectView,

    UpdateProjectView,

    DeleteProjectView
)

urlpatterns = [

    path(
        "",
        GetProjectsView.as_view()
    ),

    path(
        "create/",
        CreateProjectView.as_view()
    ),

    path(
        "<str:id>/",
        GetProjectView.as_view()
    ),

    path(
        "update/<str:id>/",
        UpdateProjectView.as_view()
    ),

    path(
        "delete/<str:id>/",
        DeleteProjectView.as_view()
    )
]