from objects.plan import Plan
from objects.curriculum import Curriculum
from config.lops21_curriculum import lops21_curriculum

from services.validation_service import ValidationService
from services.meb_validation_service import MebValidationService

from repositories.plan_repository import PlanRepository


class PlanService:
    def __init__(self, user_service):
        self._curriculum = Curriculum(lops21_curriculum())
        self._plan = None
        self._user_service = user_service

    def create_empty_plan_for_user(self):
        user = self._user_service.get_current_user()
        if user:
            self._plan = Plan(self._curriculum, user)
            plan_dict = self.get_study_plan()
            PlanRepository().save_full_plan(user, plan_dict)

    def read_plan_for_user(self):
        user = self._user_service.get_current_user()
        if user:
            old_study = PlanRepository().return_plan(user)
            self.import_study_plan(old_study)

    def add_course(self, course_code, name=None, ects_credits=0, in_cur=True):
        current_user = self._user_service.get_current_user()
        if current_user:
            if in_cur:
                course = self._plan.add_curriculum_course_to_plan(course_code)
            else:
                course = self._plan.add_own_course_to_plan(course_code, name, ects_credits)

            if course:
                PlanRepository().add_course(current_user, course)
                return True

        return False

    def delete_course(self, course_code):
        current_user = self._user_service.get_current_user()
        if current_user:
            if self._plan.delete_course_from_plan(course_code):
                PlanRepository().delete_course(current_user, course_code)

        return False

    def get_curriculum_tree(self):
        return self._plan.get_curriculum_tree()

    def get_course_status(self, course_code):
        return self._plan.check_if_course_on_plan(course_code)

    def get_stats(self):
        total_credits = self._plan.get_total_credits_on_plan()
        mandatory_credits = self._plan.get_credits_by_criteria(mandatory=True,
                                                              national=True)

        national_voluntary_credits = self._plan.get_credits_by_criteria(mandatory=False,
                                                                       national=True)

        local_voluntary_credits = self._plan.get_credits_by_criteria(mandatory=False,
                                                                    national=False)

        local_voluntary_credits += self._plan.get_credits_own_course()

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
        if self._curriculum.get_subject_code_from_course_code(course_code):
            return True

        return False

    def validate_plan(self):
        validation_service = ValidationService()
        validation_status = validation_service.validate(
            self._plan, self._curriculum)

        return validation_status

    def get_courses(self):
        return_print = []
        courses = self._plan.get_courses_on_plan()
        for course in courses:
            return_print.append(str(course))

        return return_print

    def get_own_courses(self):
        return self._plan.get_own_courses_on_plan()

    def add_exam_meb(self, exam_code, exam_period):
        current_user = self._user_service.get_current_user()
        if current_user:
            if self._plan.add_exam_to_meb_plan(exam_code, exam_period):
                PlanRepository().add_meb_exam(current_user, exam_code, exam_period)
                return True
        return False

    def remove_exam_meb(self, exam_code, exam_period):
        current_user = self._user_service.get_current_user()
        if current_user:
            if self._plan.remove_exam_from_meb_plan(exam_code, exam_period):
                PlanRepository().delete_meb_exam(current_user, exam_code, exam_period)
                return True

        return False

    def validate_meb(self):
        validation_service = MebValidationService()
        return validation_service.validate(self._plan)

    def get_study_plan(self):
        return self._plan.return_study_plan()

    def import_study_plan(self, study_plan_dict):
        current_user = self._user_service.get_current_user()
        if current_user:
            new_plan = Plan(self._curriculum, current_user)
            self._plan = new_plan

            if self._plan.import_study_plan(study_plan_dict):
                PlanRepository().save_full_plan(current_user, study_plan_dict)
                return True

        return False

    def get_meb_plan(self):
        return self._plan.return_meb_plan()

    def change_special_task_status(self, new_status):
        current_user = self._user_service.get_current_user()
        if current_user:
            self._plan.change_special_task(new_status)
            PlanRepository().change_special_task(current_user, new_status)

    def get_special_task_status(self):
        return self._plan.is_special_task()


    def get_config(self):
        return [{"special_task": self._plan.is_special_task()}]
