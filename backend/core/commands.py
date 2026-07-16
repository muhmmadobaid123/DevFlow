class Command:

    def execute(self):
        pass


class CreateTaskCommand(
    Command
):

    def execute(self):

        return (
            "Task Created"
        )


class DeleteTaskCommand(
    Command
):

    def execute(self):

        return (
            "Task Deleted"
        )