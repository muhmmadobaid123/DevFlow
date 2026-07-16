from django.urls import path

from .views import (
    NotificationListView,
    MarkAsReadView
)

urlpatterns = [

    path(
        "",
        NotificationListView.as_view()
    ),

    path(
        "<str:id>/read/",
        MarkAsReadView.as_view()
    ),
]