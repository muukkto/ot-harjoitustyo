from objects.plan import Plan
from objects.curriculum import Curriculum


class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        print(self.check_total_credits(plan, curriculum))
        # print(self.check_mandatory_credits_one_subject(plan, curriculum, "AI", 1))
        # print(self.check_mandatory_credits_one_subject(plan, curriculum, "AI", 0.5))

        print(self.check_mandatory_credits(plan, curriculum))

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
