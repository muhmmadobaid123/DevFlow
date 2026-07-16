from django.core.mail import (
    send_mail
)


class EmailService:

    @staticmethod
    def send_email(

        email,

        subject,

        message

    ):

        send_mail(

            subject,

            message,

            "admin@devflow.com",

            [email]

        )