from django.urls import path

from .views import (

    CreateSprintView,

    GetSprintsView,

    GetSprintView,

    UpdateSprintView,

    DeleteSprintView,

    CloseSprintView
)

urlpatterns = [

    path(
        "",
        GetSprintsView.as_view()
    ),

    path(
        "create/",
        CreateSprintView.as_view()
    ),

    path(
        "<str:id>/",
        GetSprintView.as_view()
    ),

    path(
        "update/<str:id>/",
        UpdateSprintView.as_view()
    ),

    path(
        "delete/<str:id>/",
        DeleteSprintView.as_view()
    ),

    path(
        "close/<str:id>/",
        CloseSprintView.as_view()
    )
]