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
            hasattr(
                request,
                "user"
            )
            and
            request.user.role
            ==
            "Admin"
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
            hasattr(
                request,
                "user"
            )
            and
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
            hasattr(
                request,
                "user"
            )
            and
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
            hasattr(
                request,
                "user"
            )
            and
            request.user.role
            ==
            "QA"
        )


class IsClient(
    BasePermission
):

    def has_permission(
        self,
        request,
        view
    ):

        return (
            hasattr(
                request,
                "user"
            )
            and
            request.user.role
            ==
            "Client"
        )