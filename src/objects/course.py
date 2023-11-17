class Course:
    def __init__ (self, code: str, subject: str):
        self.code = code
        self.subject = subject
        self.status = False
    
    def change_status(self, new_status: bool):
        self.status = new_status

    def __str__(self):
        return self.code