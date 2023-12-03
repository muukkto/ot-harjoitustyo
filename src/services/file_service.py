from tkinter import filedialog as fd

class FileService:
    def import_courses_from_txt(self, file_path):
        with open(file_path, "r", encoding="UTF-8") as file:
            courses = file.readlines()

            course_list = []

            for course in courses:
                course_list.append(course.strip())

        return course_list

    def export_plan_to_json(self, plan_service):

        print("filedialog")

        filetypes = (('Plan file (*.json)', '*.json'),)
        f = fd.asksaveasfile(mode='w', filetypes=filetypes, initialdir="C:/")

        print(f)
        print(plan_service.get_study_plan())

    def import_plan_from_json(self, plan_service):
        import_json = {'special_task': False, 
                       'courses': [{'on_cur': True, 'code': 'AI1', 'subject': 'AI', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'AI2', 'subject': 'AI', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'AI7', 'subject': 'AI', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'RUB1', 'subject': 'RUB', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'RUB5', 'subject': 'RUB', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'ENA1', 'subject': 'ENA', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'ENA2', 'subject': 'ENA', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'ENA6', 'subject': 'ENA', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'MAA2', 'subject': 'MAA', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'MAA3', 'subject': 'MAA', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'MAA4', 'subject': 'MAA', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'MAA6', 'subject': 'MAA', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'MAA9', 'subject': 'MAA', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'ET4', 'subject': 'ET', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'BI1', 'subject': 'BI', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'BI3', 'subject': 'BI', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'GE2', 'subject': 'GE', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'FY1', 'subject': 'FY', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'FY2', 'subject': 'FY', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'KE1', 'subject': 'KE', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'HI2', 'subject': 'HI', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'YH3', 'subject': 'YH', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'TE2', 'subject': 'TE', 'name': None, 'ects': 0}, {'on_cur': True, 'code': 'LI3', 'subject': 'LI', 'name': None, 'ects': 0}, 
                                   {'on_cur': True, 'code': 'OP1', 'subject': 'OP', 'name': None, 'ects': 0}], 
                        'meb_plan': {1: ["A"], 2: ["M"], 3: ["EA"]}}
        
        print(plan_service.import_study_plan(import_json))