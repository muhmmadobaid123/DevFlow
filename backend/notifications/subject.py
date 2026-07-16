class NotificationSubject:

    def __init__(self):

        self.observers = []

    def attach(self, observer):

        self.observers.append(
            observer
        )

    def notify(self, message):

        for observer in self.observers:

            observer.update(
                message
            )