from django.urls import path

from .views import *

urlpatterns = [

    path(
        "",
        GetBugsView.as_view()
    ),

    path(
        "create/",
        CreateBugView.as_view()
    ),

    path(
        "<str:id>/",
        GetBugView.as_view()
    ),

    path(
        "assign/<str:id>/",
        AssignBugView.as_view()
    ),

    path(
        "resolve/<str:id>/",
        ResolveBugView.as_view()
    ),

    path(
        "verify/<str:id>/",
        VerifyBugView.as_view()
    ),

    path(
        "delete/<str:id>/",
        DeleteBugView.as_view()
    )
]