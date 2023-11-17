class FileHandler:
    def import_courses_from_txt(self, file_path):
        file = open(file_path)
        courses = file.readlines()

        course_list = []

        for course in courses:
            course_list.append(course.strip())

        return course_list