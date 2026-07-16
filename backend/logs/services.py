from .models import ActivityLog


class AuditService:

    @staticmethod
    def log(

        user_id,

        action,

        module

    ):

        ActivityLog(

            user_id=user_id,

            action=action,

            module=module

        ).save()