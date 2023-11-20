from objects.plan import Plan
from objects.curriculum import Curriculum

from services.special_validation_service import SpecialValidationService


class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        validation_problems = []

        self.check_total_credits(plan, curriculum, validation_problems)
        self.check_national_voluntary_credits(plan, curriculum, validation_problems)
        self.check_mandatory_credits(plan, curriculum, validation_problems)

        if plan.is_special_task():
            special_validator = SpecialValidationService()
            special_plan_problems = special_validator.validate(plan, curriculum)

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
            validation_problems.append({"name": "not_enough_credits", "details": total_credits})

    def check_mandatory_credits(self, plan, curriculum, validation_problems):
        simple_subjects = curriculum.rules["national_mandatory_subjects"]
        group_subjects = [
            "mother_tongue",
            "second_national_language",
            "long_foreign_language",
            "maths",
            "worldview"
        ]
        basket_subjects = curriculum.rules["basket_subjects"]

        mandatory_credits_problems = []

        for subject in simple_subjects:
            if not self.check_mandatory_credits_one_subject(plan, curriculum, subject):
                mandatory_credits_problems.append(
                    {"name": "problem_with_simple_subjects", "details": subject})

        for group in group_subjects:
            if not self.check_mandatory_credits_one_group(plan, curriculum, group):
                mandatory_credits_problems.append(
                    {"name": "problem_with_group_subjects", "details": group})

        for basket in basket_subjects.items():
            if not self.check_mandatory_credits_one_basket(plan, basket):
                mandatory_credits_problems.append(
                    {"name": "problem_with_basket_subjects", "details": basket[0]})

        if len(mandatory_credits_problems) != 0:
            validation_problems.append({"name": "not_all_compulsory_credits",
                                        "details": mandatory_credits_problems})

    def check_national_voluntary_credits(self, plan, curriculum, validation_problems):
        voluntary_credit_rule = curriculum.rules["minimum_national_voluntary_credits"]
        voluntary_credits = plan.get_credits_by_criteria(
            mandatory=False, national=True)

        if voluntary_credits < voluntary_credit_rule:
            validation_problems.append({"name": "not_enough_national_voluntary_credits",
                                        "details": voluntary_credits})

    def check_mandatory_credits_one_basket(self, plan, basket):
        plan_total_mandatory_credits = 0
        basket_rules = basket[1]

        for subject in basket_rules["subjects"]:
            ects_credits = plan.get_mandatory_credits_subject(subject)
            if ects_credits < basket_rules["minimum_compulsory_per_subject"]:
                return False

            plan_total_mandatory_credits += ects_credits

        if plan_total_mandatory_credits >= basket_rules["minimum_compulsory_total"]:
            print(f"{basket[0]} basket OK")
            return True

        print(f"{basket[0]} basket missing")
        return False

    def check_mandatory_credits_one_subject(self, plan, curriculum, subject):
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = plan.get_mandatory_credits_subject(subject)

        if curriculum_mandatory_credits <= plan_mandatory_credits:
            print(f"{subject} OK")
            return True

        print(f"{subject} missing")
        return False

    def check_mandatory_credits_one_group(self, plan, curriculum, group):
        subject_list = curriculum.rules[group]
        subject_status = False
        for subject in subject_list:
            if self.check_mandatory_credits_one_subject(plan, curriculum, subject):
                subject_status = True

        if subject_status:
            print(f"{group} OK")
            return True

        print(f"{group} missing")
        return False
