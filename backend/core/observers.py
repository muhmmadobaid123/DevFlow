class Observer:

    def update(
        self,
        message
    ):
        pass


class EmailObserver(
    Observer
):

    def update(
        self,
        message
    ):

        print(
            f"Email Sent: {message}"
        )


class NotificationObserver(
    Observer
):

    def update(
        self,
        message
    ):

        print(
            f"Notification Sent: {message}"
        )


class Subject:

    def __init__(self):

        self.observers = []

    def attach(
        self,
        observer
    ):

        self.observers.append(
            observer
        )

    def notify(
        self,
        message
    ):

        for observer in self.observers:

            observer.update(
                message
            )