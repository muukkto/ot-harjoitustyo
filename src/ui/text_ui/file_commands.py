from pathlib import Path

from services.file_service import FileService

def import_courses_txt(plan_service):
    file_service = FileService()
    dirname = Path(__file__).parent.parent.parent

    plans = {1: "list_of_subjects_in_valid_plan.txt",
             2: "list_of_subjects_45_credits.txt",
             3: "list_of_subjects_valid_special_task.txt"}

    print("Plan alternatives:\n1 - a valid plan\n2 - plan with only 45 credits\n3 - a valid special task plan")
    plan_id = int(input("Which plan do you want: "))

    file_name = plans[plan_id]

    file_path = dirname.joinpath(f"help_files/{file_name}")
    course_list = file_service.import_courses_from_txt(file_path)
    plan_service.add_multiple_courses(course_list)

def import_plan_json(plan_service):
    file_service = FileService()

    file_service.import_plan_from_json(plan_service)

def export_plan_json(plan_service):
    file_service = FileService()

    file_service.export_plan_to_json(plan_service)

def file_handler(plan_service):
    print("1: import plan (JSON)\n2: export plan (JSON)\n3: import courses (txt)")
    match int(input("Choose command: ")):
        case 1:
            import_plan_json(plan_service)
        case 2:
            export_plan_json(plan_service)
        case 3:
            import_courses_txt(plan_service)
        case _:
            print("Command not found")
