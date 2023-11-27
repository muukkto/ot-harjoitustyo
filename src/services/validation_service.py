from objects.plan import Plan
from objects.curriculum import Curriculum

from services.special_validation_service import SpecialValidationService
from services.validation_functions import ValidationFunctions


class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        validation_problems = []

        self.check_total_credits(plan, curriculum, validation_problems)
        self.check_national_voluntary_credits(
            plan, curriculum, validation_problems)
        self.check_mandatory_credits_new(plan, curriculum, validation_problems)

        if plan.is_special_task():
            special_validator = SpecialValidationService()
            special_plan_problems = special_validator.validate(
                plan, curriculum)

            if len(special_plan_problems) != 0:
                validation_problems.append({"name": "special_task_problems",
                                            "details": special_plan_problems})
            else:
                validation_problems = []

        return validation_problems

    def check_total_credits(self, plan, curriculum, validation_problems):
        total_credit_rule = curriculum.rules["minimum_credits"]
        total_credits = plan.get_total_credits_on_plan()

        if total_credits < total_credit_rule:
            validation_problems.append(
                {"name": "not_enough_credits", "details": total_credits})

    def check_mandatory_credits_new(self, plan, curriculum, validation_problems):
        validation_functions = ValidationFunctions()
        mandatory_credits_problems = []

        missing_credits = validation_functions.check_total_mandatory(
            plan, curriculum, mandatory_credits_problems)

        if missing_credits != 0:
            validation_problems.append({"name": "not_all_compulsory_credits",
                                        "details": mandatory_credits_problems})

    def check_national_voluntary_credits(self, plan, curriculum, validation_problems):
        voluntary_credit_rule = curriculum.rules["minimum_national_voluntary_credits"]
        voluntary_credits = plan.get_credits_by_criteria(
            mandatory=False, national=True)

        if voluntary_credits < voluntary_credit_rule:
            validation_problems.append({"name": "not_enough_national_voluntary_credits",
                                        "details": voluntary_credits})
