class Course:
    def __init__(self, code: str, subject: str):
        self.code = code
        self.subject = subject
        self.on_plan = False

    def change_status(self, new_status: bool):
        self.on_plan = new_status

    def status(self):
        return self.on_plan

    def __str__(self):
        return self.code
