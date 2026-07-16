class Observer:

    def update(self, message):
        pass


class NotificationObserver(
    Observer
):

    def update(self, message):

        print(
            f"Notification: {message}"
        )