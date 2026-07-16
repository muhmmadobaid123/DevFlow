class LowPriorityStrategy:

    def execute(self):

        return "Low Priority Task"


class MediumPriorityStrategy:

    def execute(self):

        return "Medium Priority Task"


class HighPriorityStrategy:

    def execute(self):

        return "High Priority Task"


class PriorityContext:

    def __init__(self, strategy):

        self.strategy = strategy

    def run(self):

        return self.strategy.execute()