from objects.plan import Plan
from objects.curriculum import Curriculum

class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        self.check_total_credits(plan, curriculum, curriculum.rules())

    def check_total_credits(self, plan, curriculum, total_credit_rule):
        total_credits = 0

        for course in plan.get_courses_on_plan():
            if course.status:
                total_credits += curriculum.get_credits_from_course_code(course.code)

        return total_credits >= total_credit_rule
    