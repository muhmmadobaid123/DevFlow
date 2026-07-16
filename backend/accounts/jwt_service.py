from rest_framework_simplejwt.tokens import (
    RefreshToken
)


class JWTService:

    @staticmethod
    def create_tokens(user):

        refresh = RefreshToken()

        refresh["user_id"] = (
            str(user.id)
        )

        refresh["role"] = (
            user.role
        )

        return {

            "access":
            str(
                refresh.access_token
            ),

            "refresh":
            str(refresh)
        }