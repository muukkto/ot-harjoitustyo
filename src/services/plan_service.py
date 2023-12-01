from objects.plan import Plan
from objects.curriculum import Curriculum
from config.lops21_curriculum import lops21_curriculum

from services.validation_service import ValidationService
from services.meb_validation_service import MebValidationService


class PlanService:
    def __init__(self):
        self.curriculum = Curriculum(lops21_curriculum())
        self.plan = Plan(self.curriculum)

    def add_course(self, course_code, name=None, ects_credits=0, in_cur=True):
        if in_cur:
            return self.plan.add_curriculum_course_to_plan(course_code)

        return self.plan.add_own_course_to_plan(course_code, name, ects_credits)

    def add_multiple_courses(self, courses: list):
        for course in courses:
            self.add_course(course)

    def delete_course(self, course_code):
        return self.plan.delete_course_from_plan(course_code)

    def print_stats(self):
        total_credits = self.plan.get_total_credits_on_plan()
        mandatory_credits = self.plan.get_credits_by_criteria(mandatory=True,
                                                              national=True)

        national_voluntary_credits = self.plan.get_credits_by_criteria(mandatory=False,
                                                                       national=True)

        local_voluntary_credits = self.plan.get_credits_by_criteria(mandatory=False,
                                                                    national=False)

        local_voluntary_credits += self.plan.get_credits_own_course()

        return_print = []
        return_print.append(
            f"Total credits: {total_credits}")
        return_print.append(
            f"Mandatory credits: {mandatory_credits}")
        return_print.append(
            f"National voluntary credits: {national_voluntary_credits}")
        return_print.append(
            f"Local voluntary credits: {local_voluntary_credits}")

        return return_print

    def check_reserved_codes(self, course_code):
        if self.curriculum.get_subject_code_from_course_code(course_code):
            return True

        return False

    def validation_print(self, status):
        print(status)

    def validate_plan(self):
        validation_service = ValidationService()
        validation_status = validation_service.validate(
            self.plan, self.curriculum)
        self.validation_print(validation_status)

    def print_courses(self):
        return_print = []
        courses = self.plan.get_courses_on_plan()
        for course in courses:
            return_print.append(str(course))

        return return_print

    def add_exam_meb(self, exam_code, exam_period):
        return self.plan.add_exam_to_meb_plan(exam_code, exam_period)

    def remove_exam_meb(self, exam_code, exam_period):
        return self.plan.remove_exam_from_meb_plan(exam_code, exam_period)

    def validate_meb(self):
        validation_service = MebValidationService()
        validation_service.validate(self.plan)

    def get_meb_plan(self):
        return self.plan.return_meb_plan()
