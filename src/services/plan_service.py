from objects.plan import Plan
from objects.curriculum import Curriculum
from config.lops21_curriculum import lops21_curriculum

from services.validation_service import ValidationService


class PlanService:
    def __init__(self):
        self.curriculum = Curriculum(lops21_curriculum())
        self.plan = Plan(self.curriculum)

    def add_course(self, course_code):
        self.plan.add_existing_course_to_plan(course_code)

    def add_multiple_courses(self, courses: list):
        for course in courses:
            self.add_course(course)

    def delete_course(self, course_code):
        self.plan.delete_course_from_plan(course_code)

    def print_stats(self):
        print("STATS")

    def validate_plan(self):
        validation_service = ValidationService()
        validation_service.validate(self.plan, self.curriculum)

    def print_courses(self):
        courses = self.plan.get_courses_on_plan()
        for course in courses:
            print(course)
