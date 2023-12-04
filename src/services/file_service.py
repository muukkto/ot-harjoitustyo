import json

class FileService:
    def import_courses_from_txt(self, file_path):
        with open(file_path, "r", encoding="UTF-8") as file:
            courses = file.readlines()

            course_list = []

            for course in courses:
                course_list.append(course.strip())

        return course_list

    def export_plan_to_json(self, plan_service, file_path):

        study_plan_dict = plan_service.get_study_plan()

        json_object = json.dumps(study_plan_dict, indent=4)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(json_object)

    def import_plan_from_json(self, plan_service, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            import_json = file.read()

        import_dict = json.loads(import_json)

        import_meb_plan = import_dict["meb_plan"]
        new_meb_plan = {}

        for (period, subjects) in import_meb_plan.items():
            new_meb_plan[int(period)] = subjects

        import_dict["meb_plan"] = new_meb_plan

        return plan_service.import_study_plan(import_dict)
