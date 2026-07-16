class Report:

    def __init__(self):

        self.data = {}

    def add(self, key, value):

        self.data[key] = value

    def build(self):

        return self.data


class ReportBuilder:

    def __init__(self):

        self.report = Report()

    def project_count(self, count):

        self.report.add(
            "total_projects",
            count
        )

    def sprint_count(self, count):

        self.report.add(
            "total_sprints",
            count
        )

    def task_count(self, count):

        self.report.add(
            "total_tasks",
            count
        )

    def bug_count(self, count):

        self.report.add(
            "total_bugs",
            count
        )

    def get_report(self):

        return self.report.build()