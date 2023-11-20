from objects.plan import Plan
from objects.curriculum import Curriculum
from config.lops21_curriculum import lops21_curriculum

from services.validation_service import ValidationService


class PlanService:
    def __init__(self):
        self.curriculum = Curriculum(lops21_curriculum())
        self.plan = Plan(self.curriculum)

    def add_course(self, course_code, name=None, ects_credits=0, in_cur=True):
        if in_cur:
            self.plan.add_curriculum_course_to_plan(course_code)
        else:
            self.plan.add_own_course_to_plan(course_code, name, ects_credits)

    def add_multiple_courses(self, courses: list):
        for course in courses:
            self.add_course(course)

    def delete_course(self, course_code):
        self.plan.delete_course_from_plan(course_code)

    def print_stats(self):
        return_print = []
        return_print.append(f"Total credits: {self.plan.get_total_credits_on_plan()}")

        return return_print

    def print_curriculum(self):
        return_print = self.curriculum.return_all_courses()
        return return_print

    def validate_plan(self):
        validation_service = ValidationService()
        validation_service.validate(self.plan, self.curriculum)

    def print_courses(self):
        return_print = []
        courses = self.plan.get_courses_on_plan()
        for course in courses:
            return_print.append(str(course))

        return return_print
