class FileHandler:
    def import_courses_from_txt(self, file_path):
        with open(file_path, "r", encoding="UTF-8") as file:
            courses = file.readlines()

            course_list = []

            for course in courses:
                course_list.append(course.strip())

        return course_list
