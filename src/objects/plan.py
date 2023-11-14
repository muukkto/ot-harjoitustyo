from objects.course import Course
from objects.curriculum import Curriculum

class Plan:
    def __init__ (self, curriculum: Curriculum):
        self.curriculum = curriculum
        self.courses_plan = {}

        for subject in curriculum.subjects.items():
            subject_code = subject[0]
            subject_courses = subject[1]

            self.courses_plan[subject_code] = {}

            for course in subject_courses["courses"]:
                self.courses_plan[subject_code][course] = Course(course)

    def add_existing_course_to_plan (self, code):
        course = self.find_course(code)
        if course:
            course.change_status(True)

    def add_new_course_to_plan (self, code, description, credits):
        pass
    
    def delete_course_from_plan (self, code):
        course = self.find_course(code)
        if course:
            course.change_status(False)


    def find_course (self, code):
        for subject in self.curriculum.return_all_subject_codes():
            if(code.find(subject)!=-1):
                if(code in self.courses_plan[subject]):
                    return self.courses_plan[subject][code]
                else:
                    return False
        
        return False

    def print_courses_on_plan (self):
        for subject in self.courses_plan.values():
            for course in subject.values():
                if course.status:
                    print(course)