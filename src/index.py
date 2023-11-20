from pathlib import Path

from services.plan_service import PlanService
from services.file_service import FileHandler


def print_commands():
    print("1: add course to your plan")
    print("2: delete course from your plan")
    print("3: import courses from file")
    print("4: print courses added to your plan")
    print("5: validate plan")
    print("6: print stats")
    print("7: print courses on curriculum")
    print("10: exit the program")


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
    # pylint: disable=too-many-arguments
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
                # vaihda tiedotstonimeksi haluamasia
                # suunnitelman jolla validiointi menee läpi: "list_of_subjects_in_valid_plan.txt"
                # suunnitelma jolla tilastoissa on 45 credits: "list_of_subjects_45_credits.txt"
                import_courses(
                    "list_of_subjects_45_credits.txt", plan_service)
            case 4:
                print_list(plan_service.print_courses())
            case 5:
                plan_service.validate_plan()
            case 6:
                print_list(plan_service.print_stats())
            case 7:
                print_list(plan_service.print_curriculum())
            case 8:
                print("exiting...")
                break
            case _:
                print("Command not found")


if __name__ == "__main__":
    main()
