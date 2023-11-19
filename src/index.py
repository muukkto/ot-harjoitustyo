from pathlib import Path

from services.plan_service import PlanService
from services.file_service import FileHandler


def print_commands():
    print("1: add course to your plan")
    print("2: delete course from your plan")
    print("3: print courses added to your plan")
    print("4: validate plan")
    print("5: import courses from file")
    print("6: print stats")
    print("8: exit the program")


def import_courses(file_name, plan_service):
    file_handler = FileHandler()
    dirname = Path(__file__).parent

    file_path = dirname.joinpath(f"help_files/{file_name}")
    course_list = file_handler.import_courses_from_txt(file_path)
    plan_service.add_multiple_courses(course_list)


def add_course(plan_service):
    course_code = input("Which course do you want to add to your plan? ")
    plan_service.add_course(course_code)


def delete_course(plan_service):
    course_code = input("Which course do you want to remove from your plan? ")
    plan_service.delete_course(course_code)

def print_list(output_list):
    for row in output_list:
        print(row)


def main():
    plan_service = PlanService()
    while True:
        match int(input("Choose command (0 for help): ")):
            case 0:
                print_commands()
            case 1:
                add_course(plan_service)
            case 2:
                delete_course(plan_service)
            case 3:
                print_list(plan_service.print_courses())
            case 4:
                plan_service.validate_plan()
            case 5:
                import_courses("list_of_subjects_45_credits.txt", plan_service)
            case 6:
                print_list(plan_service.print_stats())
            case 8:
                break
            case _:
                print("Command not found")


if __name__ == "__main__":
    main()
