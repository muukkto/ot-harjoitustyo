from objects.plan import Plan
from objects.curriculum import Curriculum


class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        print(self.check_total_credits(plan, curriculum))
        #print(self.check_mandatory_credits_one_subject(plan, curriculum, "AI", 1))
        #print(self.check_mandatory_credits_one_subject(plan, curriculum, "AI", 0.5))

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

        for subject in simple_subjects:
            if self.check_mandatory_credits_one_subject(plan, curriculum, subject):
                print(f"{subject} OK")
            else:
                print(f"{subject} missing")

        for group in group_subjects:
            subject_list = curriculum.rules[group]
            subject_status = False
            for subject in subject_list:
                if self.check_mandatory_credits_one_subject(plan, curriculum, subject):
                    subject_status = True

            if subject_status:
                print(f"{group} OK")
            else:
                print(f"{group} missing")

        for basket in basket_subjects.items():
            if self.check_mandatory_credits_basket(plan, curriculum, basket[1]):
                print(f"{basket[0]} basket OK")
            else:
                print(f"{basket[0]} basket missing")


    def get_mandatory_credits_on_plan(self, plan, curriculum_subject_courses):
        plan_mandatory_credits = 0

        for course_code in curriculum_subject_courses:
            if curriculum_subject_courses[course_code]["mandatory"]:
                if plan.check_if_course_on_plan(course_code):
                    plan_mandatory_credits += curriculum_subject_courses[course_code]["credits"]

        return plan_mandatory_credits

    def check_mandatory_credits_basket(self, plan, curriculum, basket):
        plan_total_mandatory_credits = 0

        for subject in basket["subjects"]:
            subject_courses = curriculum.subjects[subject]["courses"]
            ects_credits = self.get_mandatory_credits_on_plan(plan, subject_courses)
            if ects_credits < basket["minimum_compulsory_per_subject"]:
                return False

            plan_total_mandatory_credits += ects_credits

        if plan_total_mandatory_credits >= basket["minimum_compulsory_total"]:
            return True

        return False

    def check_mandatory_credits_one_subject(self, plan, curriculum, subject_code):
        subject_courses = curriculum.subjects[subject_code]["courses"]
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(subject_code)
        plan_mandatory_credits = self.get_mandatory_credits_on_plan(plan, subject_courses)

        if curriculum_mandatory_credits <= plan_mandatory_credits:
            return True

        return False
