from services.plan_service import PlanService
from services.file_service import FileHandler

from pathlib import Path

def print_commands():
    print("1: add course to your plan")
    print("2: delete course from your plan")
    print("3: print courses added to your plan")
    print("4: validate plan")
    print("5: import courses from file")
    print("8: exit the program")

def main():
    plan_service = PlanService()
    file_handler = FileHandler()

    while True:
        command = int(input("Choose command (0 for help): "))

        if command == 0:
            print_commands()
        elif command == 1:
            course_code = input("Which course do you want to add to your plan? ")
            plan_service.add_course(course_code)
        elif command == 2:
            course_code = input("Which course do you want to remove from your plan? ")
            plan_service.delete_course(course_code)
        elif command == 3:
            plan_service.print_courses()
        elif command == 4:
            plan_service.validate_plan()
        elif command == 5:
            dirname = Path(__file__).parent
            file_path = dirname.joinpath("help_files/list_of_subjects_45_credits.txt")
            course_list = file_handler.import_courses_from_txt(file_path)
            plan_service.add_multiple_courses(course_list)

        elif command == 8:
            break
        else:
            print("Command not found")


if __name__ == "__main__":
    main()