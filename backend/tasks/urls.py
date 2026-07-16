from django.urls import path

from .views import (

    CreateTaskView,

    GetTasksView,

    GetTaskView,

    UpdateTaskView,

    DeleteTaskView,

    ChangeTaskStatusView
)

urlpatterns = [

    path(
        "",
        GetTasksView.as_view()
    ),

    path(
        "create/",
        CreateTaskView.as_view()
    ),

    path(
        "<str:id>/",
        GetTaskView.as_view()
    ),

    path(
        "update/<str:id>/",
        UpdateTaskView.as_view()
    ),

    path(
        "delete/<str:id>/",
        DeleteTaskView.as_view()
    ),

    path(
        "status/<str:id>/",
        ChangeTaskStatusView.as_view()
    )
]