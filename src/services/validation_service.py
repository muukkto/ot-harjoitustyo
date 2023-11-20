from objects.plan import Plan
from objects.curriculum import Curriculum


class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        validation_criterias = {
            "enough_credits": False,
            "all_compulsory_credits": False,
            "enough_national_voluntary_credits": False,
            "enough_special_task_credits": False,
            "not_too_much_excluded_courses": False
        }

        validation_criterias["enough_credits"] = self.check_total_credits(
            plan, curriculum)
        validation_criterias["all_compulsory_credits"] = self.check_mandatory_credits(
            plan, curriculum)
        validation_criterias["enough_national_voluntary_credits"] = self.check_national_voluntary_credits(
            plan, curriculum)

        if validation_criterias["enough_credits"]:
            if validation_criterias["enough_national_voluntary_credits"]:
                if validation_criterias["all_compulsory_credits"]:
                    return True

                if plan.is_special_task():
                    validation_criterias["enough_special_task_credits"] = self.check_special_task_credits(
                        plan, curriculum)
                    validation_criterias["not_too_much_excluded_courses"] = self.check_excluded_credits(
                        plan, curriculum)
                    if validation_criterias["enough_special_task_credits"]:
                        if validation_criterias["not_too_much_excluded_courses"]:
                            return True

        return False

    def check_total_credits(self, plan, curriculum):
        total_credit_rule = curriculum.rules["minimum_credits"]
        total_credits = plan.get_total_credits_on_plan()

        return total_credits >= total_credit_rule

    def check_mandatory_credits(self, plan, curriculum):
        simple_subjects = curriculum.rules["national_mandatory_subjects"]
        group_subjects = [
            "mother_tongue",
            "second_national_language",
            "long_foreign_language",
            "maths",
            "worldview"
        ]
        basket_subjects = curriculum.rules["basket_subjects"]

        mandatory_courses_status = True

        for subject in simple_subjects:
            if not self.check_mandatory_credits_one_subject(plan, curriculum, subject):
                mandatory_courses_status = False

        for group in group_subjects:
            if not self.check_mandatory_credits_one_group(plan, curriculum, group):
                mandatory_courses_status = False

        for basket in basket_subjects.items():
            if not self.check_mandatory_credits_one_basket(plan, curriculum, basket):
                mandatory_courses_status = False

        return mandatory_courses_status

    def check_national_voluntary_credits(self, plan, curriculum):
        voluntary_credit_rule = curriculum.rules["minimum_national_voluntary_credits"]
        voluntary_credits = plan.get_credits_by_criteria(
            mandatory=False, national=True)
        if voluntary_credits >= voluntary_credit_rule:
            return True

        return False

    def get_mandatory_credits_on_plan(self, plan, curriculum_subject_courses):
        plan_mandatory_credits = 0

        for course_code in curriculum_subject_courses:
            if curriculum_subject_courses[course_code]["mandatory"]:
                if plan.check_if_course_on_plan(course_code):
                    plan_mandatory_credits += curriculum_subject_courses[course_code]["credits"]

        return plan_mandatory_credits

    def check_mandatory_credits_one_basket(self, plan, curriculum, basket):
        plan_total_mandatory_credits = 0
        basket_rules = basket[1]

        for subject in basket_rules["subjects"]:
            subject_courses = curriculum.subjects[subject]["courses"]
            ects_credits = self.get_mandatory_credits_on_plan(
                plan, subject_courses)
            if ects_credits < basket_rules["minimum_compulsory_per_subject"]:
                return False

            plan_total_mandatory_credits += ects_credits

        if plan_total_mandatory_credits >= basket_rules["minimum_compulsory_total"]:
            print(f"{basket[0]} basket OK")
            return True

        print(f"{basket[0]} basket missing")
        return False

    def check_mandatory_credits_one_subject(self, plan, curriculum, subject):
        subject_courses = curriculum.subjects[subject]["courses"]
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = self.get_mandatory_credits_on_plan(
            plan, subject_courses)

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

    def check_special_task_credits(self, plan, curriculum):
        special_task_code = curriculum.rules["special_task_code"]
        special_task_credits_rule = curriculum.rules["minimum_special_task_credits"]

        special_task_credits = plan.get_credits_by_criteria(
            mandatory=False, national=False, subject=special_task_code)

        return special_task_credits >= special_task_credits_rule

    def check_half_mandatory_credits_one_subject(self, plan, curriculum, subject):
        subject_courses = curriculum.subjects[subject]["courses"]
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = self.get_mandatory_credits_on_plan(
            plan, subject_courses)

        if curriculum_mandatory_credits / 2 > plan_mandatory_credits:
            return (False, 9999)

        return (True, curriculum_mandatory_credits - plan_mandatory_credits)

    def check_half_mandatory_credits_one_basket(self, plan, curriculum, basket):
        plan_total_mandatory_credits = 0
        basket_rules = basket[1]

        for subject in basket_rules["subjects"]:
            subject_courses = curriculum.subjects[subject]["courses"]
            ects_credits = self.get_mandatory_credits_on_plan(
                plan, subject_courses)
            if ects_credits < basket_rules["minimum_compulsory_per_subject"]/2:
                return (False, 9999)

            plan_total_mandatory_credits += ects_credits

        return (True, basket_rules["minimum_compulsory_total"] - plan_total_mandatory_credits)

    def check_half_mandatory_credits_one_group(self, plan, curriculum, group):
        subject_list = curriculum.rules[group]
        subject_status = False
        least_exluded = 9999

        for subject in subject_list:
            subject_return = self.check_half_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if subject_return[0]:
                subject_status = True
                least_exluded = min(subject_return[1], least_exluded)

        if subject_status:
            return (True, least_exluded)

        return (False, 9999)

    def check_excluded_credits(self, plan, curriculum):
        simple_subjects = curriculum.rules["national_mandatory_subjects"]
        group_subjects = [
            "mother_tongue",
            "second_national_language",
            "long_foreign_language",
            "maths",
            "worldview"
        ]
        basket_subjects = curriculum.rules["basket_subjects"]
        mandatory_courses_excluded_rule = curriculum.rules["maximum_excluded_credits_special_task"]

        all_mandatory_courses_atleast_half = True
        mandatory_courses_excluded_credits = 0

        for subject in simple_subjects:
            subject_return = self.check_half_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if not subject_return[0]:
                all_mandatory_courses_atleast_half = False

            mandatory_courses_excluded_credits += subject_return[1]

        for group in group_subjects:
            group_return = self.check_half_mandatory_credits_one_group(
                plan, curriculum, group)
            if not group_return[0]:
                all_mandatory_courses_atleast_half = False

            mandatory_courses_excluded_credits += group_return[1]

        for basket in basket_subjects.items():
            basket_return = self.check_half_mandatory_credits_one_basket(
                plan, curriculum, basket)
            if not basket_return[0]:
                all_mandatory_courses_atleast_half = False

            mandatory_courses_excluded_credits += basket_return[1]

        if all_mandatory_courses_atleast_half:
            if mandatory_courses_excluded_credits <= mandatory_courses_excluded_rule:
                return True

        return False
