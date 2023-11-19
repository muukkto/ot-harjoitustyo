class Course:
    def __init__(self, code: str,
                 subject: str = None,
                 on_cur: bool = True,
                 name: str = None,
                 ects: int = 0):

        self.code = code
        self.on_cur = on_cur
        if on_cur:
            self.subject = subject
            self.on_plan = False
        else:
            self.name = name
            self.ects = ects
            self.on_plan = True

    def change_status(self, new_status: bool):
        self.on_plan = new_status

    def status(self):
        return self.on_plan

    def get_ects(self):
        if not self.on_cur:
            return self.ects

        return False

    def __str__(self):
        return self.code
