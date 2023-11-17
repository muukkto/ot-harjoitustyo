from objects.plan import Plan
from objects.curriculum import Curriculum

class ValidationService:
    def validate(self, plan: Plan, curriculum: Curriculum):
        self.check_total_credits(plan, curriculum)

    def check_total_credits(self, plan, curriculum):
        total_credits = 0

        for subject in plan.courses_plan.values():
            for course in subject.values():
                if course.status:
                    total_credits += curriculum.get_credits_from_course_code(course.code)

        print(total_credits)
    