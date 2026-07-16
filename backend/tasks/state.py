class TodoState:

    def next(self):

        return "InProgress"


class InProgressState:

    def next(self):

        return "Testing"


class TestingState:

    def next(self):

        return "Done"


class DoneState:

    def next(self):

        return "Done"