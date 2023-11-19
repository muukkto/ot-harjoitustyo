from objects.plan import Plan
from objects.curriculum import Curriculum

class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        print(self.check_total_credits(plan, curriculum))
        print(self.check_mandatory_credits_one_subject(plan, curriculum, "KU", 1))

    def check_total_credits(self, plan, curriculum):
        total_credit_rule = curriculum.rules["minimum_credits"]
        total_credits = 0
        for course in plan.get_courses_on_plan():
            if course.status:
                total_credits += curriculum.get_credits_from_course_code(course.code)

        return total_credits >= total_credit_rule

    def get_amount_mandatory_credits_one_subject_in_plan(self, plan, curriculum_subject_courses):
        plan_amount_mandatory_credits = 0

        for course_code in curriculum_subject_courses:
            if curriculum_subject_courses[course_code]["mandatory"]:
                if plan.check_if_course_on_plan(course_code):
                    plan_amount_mandatory_credits += curriculum_subject_courses[course_code]["credits"]

        return plan_amount_mandatory_credits

        

    def check_mandatory_credits_one_subject(self, plan, curriculum, subject_code, percentage):
        curriculum_subject_courses = curriculum.subjects[subject_code]["courses"]
        curriculum_amount_mandatory_credits = 0
        plan_amount_mandatory_credits = 0

        for course_code in curriculum_subject_courses:
            if curriculum_subject_courses[course_code]["mandatory"]:
                curriculum_amount_mandatory_credits += curriculum_subject_courses[course_code]["credits"]

        
        print(curriculum_amount_mandatory_credits)
        print(self.get_amount_mandatory_credits_one_subject_in_plan(plan, curriculum_subject_courses))

        #print(courses_subject)
    
