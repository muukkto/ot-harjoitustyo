from services.validation_functions import ValidationFunctions


class SpecialValidationService:
    def validate(self, plan, curriculum):
        validation_problems = []

        special_task_credits_status = self.check_special_task_credits(
            plan, curriculum)
        excluded_courses_status = self.check_excluded_credits(plan, curriculum)

        validation_problems.extend(special_task_credits_status)
        validation_problems.extend(excluded_courses_status)

        return validation_problems

    def check_special_task_credits(self, plan, curriculum):
        special_task_code = curriculum.rules["special_task_code"]
        special_task_credits_rule = curriculum.rules["minimum_special_task_credits"]

        special_task_credits = plan.get_credits_by_criteria(
            mandatory=False, national=False, subject=special_task_code)

        if special_task_credits >= special_task_credits_rule:
            return []

        return [{"name": "not_enough_special_task_credits",
                 "details": special_task_credits}]

    def check_excluded_credits(self, plan, curriculum):
        mandatory_courses_excluded_rule = curriculum.rules["maximum_excluded_credits_special_task"]

        validation_functions = ValidationFunctions()

        excluded_courses_problems = []
        excluded_credits = validation_functions.check_total_mandatory(
            plan, curriculum, excluded_courses_problems)

        if len(excluded_courses_problems) == 0:
            if excluded_credits <= mandatory_courses_excluded_rule:
                return []

            excluded_courses_problems.append("too_much_excluded_courses")

        return [{"name": "too_much_excluded_courses",
                 "details": excluded_courses_problems}]
