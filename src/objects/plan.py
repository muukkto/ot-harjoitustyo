from objects.course import Course
from objects.curriculum import Curriculum


class Plan:
    def __init__(self, curriculum: Curriculum):
        self.curriculum = curriculum
        self.courses_plan = {}
        self.own_courses = {}
        self.special_task = False

        for subject in curriculum.subjects.items():
            subject_code = subject[0]
            subject_courses = subject[1]

            self.courses_plan[subject_code] = {}

            for course in subject_courses["courses"]:
                self.courses_plan[subject_code][course] = Course(
                    course, subject_code, True)

    def add_curriculum_course_to_plan(self, code):
        course = self.find_cur_course(code)
        if course:
            course.change_status(True)
            return True

        return False

    def add_own_course_to_plan(self, code, name, ects_credits):
        course = self.find_own_course(code)
        subject = self.curriculum.get_subject_code_from_course_code(code)
        if not course and not subject:
            new_course = Course(code, on_cur=False,
                                name=name, ects=ects_credits)
            self.own_courses[code] = new_course
            return True

        return False

    def delete_course_from_plan(self, code):
        course = self.find_cur_course(code)
        if course:
            course.change_status(False)
            return True

        own_course = self.find_own_course(code)
        if own_course:
            del self.own_courses[code]
            return True

        return False

    def find_cur_course(self, course_code):
        subject_code = self.curriculum.get_subject_code_from_course_code(
            course_code)

        if subject_code:
            if course_code in self.courses_plan[subject_code]:
                return self.courses_plan[subject_code][course_code]

        return None

    def find_own_course(self, course_code):
        if course_code in self.own_courses:
            return self.own_courses[course_code]

        return None

    def check_if_course_on_plan(self, course_code):
        found_course = self.find_cur_course(course_code)
        if found_course:
            return found_course.status()

        found_course_2 = self.find_own_course(course_code)
        if found_course_2:
            return found_course_2.status()

        return False

    def get_courses_on_plan(self):
        cur_courses = self.get_curriculum_courses_on_plan()
        own_courses = self.get_own_courses_on_plan()

        return cur_courses + own_courses

    def get_curriculum_courses_on_plan(self, subject_code: str = None):
        planned_courses = []

        if subject_code:
            for course in self.courses_plan[subject_code].values():
                if course.status():
                    planned_courses.append(course)
        else:
            for subject in self.courses_plan.values():
                for course in subject.values():
                    if course.status():
                        planned_courses.append(course)

        return planned_courses

    def get_own_courses_on_plan(self):
        planned_courses = []
        for course in self.own_courses.values():
            planned_courses.append(course)

        return planned_courses

    def get_credits_by_criteria(self, mandatory: bool, national: bool, subject: str = None):
        total_credits = 0
        for course in self.get_curriculum_courses_on_plan(subject):
            course_code = course.code
            course_status = self.curriculum.get_course_status_from_course_code(
                course_code)
            if course_status["mandatory"] == mandatory and course_status["national"] == national:
                course_credits = self.curriculum.get_credits_from_course_code(
                    course_code)
                total_credits += course_credits

        return total_credits

    def get_credits_own_course(self):
        total_credits = 0

        for course in self.get_own_courses_on_plan():
            total_credits += course.get_ects()

        return total_credits

    def get_mandatory_credits_subject(self, subject_code):
        return self.get_credits_by_criteria(mandatory=True, national=True, subject=subject_code)

    def get_total_credits_on_plan(self):
        total_credits = 0
        total_credits += self.get_credits_by_criteria(True, True)
        total_credits += self.get_credits_by_criteria(False, True)
        total_credits += self.get_credits_by_criteria(False, False)
        total_credits += self.get_credits_own_course()

        return total_credits

    def is_special_task(self):
        return self.special_task

    def change_special_task(self, status):
        self.special_task = status
