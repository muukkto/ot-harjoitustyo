from objects.course import Course
from objects.curriculum import Curriculum


class Plan:
    def __init__(self, curriculum: Curriculum):
        self.curriculum = curriculum
        self.courses_plan = {}

        for subject in curriculum.subjects.items():
            subject_code = subject[0]
            subject_courses = subject[1]

            self.courses_plan[subject_code] = {}

            for course in subject_courses["courses"]:
                self.courses_plan[subject_code][course] = Course(
                    course, subject_code)

    def add_existing_course_to_plan(self, code):
        course = self.find_course(code)
        if course:
            course.change_status(True)
            return True

        return False

    def add_new_course_to_plan(self, code, description, ects_credits):
        pass

    def delete_course_from_plan(self, code):
        course = self.find_course(code)
        if course:
            course.change_status(False)
            return True

        return False

    def find_course(self, course_code):
        subject_code = self.curriculum.get_subject_code_from_course_code(
            course_code)

        if subject_code:
            if course_code in self.courses_plan[subject_code]:
                return self.courses_plan[subject_code][course_code]

        return None

    def check_if_course_on_plan(self, course_code):
        found_course = self.find_course(course_code)
        if found_course:
            return found_course.status()

        return False

    def get_courses_on_plan(self):
        planned_courses = []
        for subject in self.courses_plan.values():
            for course in subject.values():
                if course.status():
                    planned_courses.append(course)

        return planned_courses

    def get_total_credits_on_plan(self):
        total_credits = 0
        for course in self.get_courses_on_plan():
            total_credits += self.curriculum.get_credits_from_course_code(
                course.code)

        return total_credits
    