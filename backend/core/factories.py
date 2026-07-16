from accounts.models import User


class UserFactory:

    @staticmethod
    def create_user(data):

        role = data["role"]

        user = User(

            name=data["name"],

            email=data["email"],

            password=data["password"],

            role=role
        )

        user.save()

        return user