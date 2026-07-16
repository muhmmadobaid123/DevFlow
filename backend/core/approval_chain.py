class Handler:

    def __init__(self):

        self.next_handler = None

    def set_next(
        self,
        handler
    ):

        self.next_handler = handler

        return handler


class PMApproval(
    Handler
):

    def handle(
        self,
        request
    ):

        if request == "Project":

            return (
                "Approved By PM"
            )

        if self.next_handler:

            return self.next_handler.handle(
                request
            )


class AdminApproval(
    Handler
):

    def handle(
        self,
        request
    ):

        return (
            "Approved By Admin"
        )