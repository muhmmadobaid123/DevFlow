from django.urls import path
from django.urls import include

urlpatterns = [

    path(
        "api/accounts/",
        include(
            "accounts.urls"
        )
    ),

    path(
        "api/projects/",
        include(
            "projects.urls"
        )
    ),

    path(
        "api/sprints/",
        include(
            "sprints.urls"
        )
    ),

    path(
        "api/tasks/",
        include(
            "tasks.urls"
        )
    ),

    path(
        "api/bugs/",
        include(
            "bugs.urls"
        )
    ),

    path(
        "api/reports/",
        include(
            "reports.urls"
        )
    ),

    path(
        "api/notifications/",
        include(
            "notifications.urls"
        )
    ),

]