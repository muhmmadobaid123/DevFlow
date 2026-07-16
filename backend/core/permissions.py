from rest_framework.permissions import (
    BasePermission
)


class IsAdmin(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.role
            == "Admin"
        )


class IsProjectManager(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.role
            ==
            "ProjectManager"
        )


class IsDeveloper(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.role
            ==
            "Developer"
        )


class IsQA(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            request.user.role
            ==
            "QA"
        )