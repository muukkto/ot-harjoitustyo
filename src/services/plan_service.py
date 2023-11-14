from objects.plan import Plan
from objects.curriculum import Curriculum
from config.lops21_curriculum import lops21_curriculum

class PlanService:
    def __init__ (self):
        self.curriculum = Curriculum(lops21_curriculum())
        self.plan = Plan(self.curriculum)

    def add_course(self):
        course_code = input("Which course do you want to add to your plan? ")
        self.plan.add_existing_course_to_plan(course_code)

    def delete_course(self):
        course_code = input("Which course do you want to remove from your plan? ")
        self.plan.delete_course_from_plan(course_code)

    def print_stats(self):
        print("STATS")

    def print_courses(self):
        self.plan.print_courses_on_plan()

