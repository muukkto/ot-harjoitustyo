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
    print("7: update matriculation examination plan")
    print("10: exit the program")


def import_courses(plan_service):
    file_handler = FileHandler()
    dirname = Path(__file__).parent

    plans = {1: "list_of_subjects_in_valid_plan.txt",
             2: "list_of_subjects_45_credits.txt",
             3: "list_of_subjects_valid_special_task.txt"}

    print("Plan alternatives:\n1 - a valid plan\n2 - plan with only 45 credits\n3 - a valid special task plan")
    plan_id = int(input("Which plan do you want: "))

    file_name = plans[plan_id]

    file_path = dirname.joinpath(f"help_files/{file_name}")
    course_list = file_handler.import_courses_from_txt(file_path)
    plan_service.add_multiple_courses(course_list)


def add_course(plan_service):
    course_code = input("Which course do you want to add to your plan?")
    if plan_service.check_reserved_codes(course_code):
        status = plan_service.add_course(course_code)
    else:
        course_name = input("What name does this course have?")
        ects_credits = int(input("How many credits (ECTS) is the course?"))
        status = plan_service.add_course(course_code, name=course_name,
                                         ects_credits=ects_credits, in_cur=False)

    if status:
        print("Course added succesfully!")
    else:
        print("Couldn't add course!")


def delete_course(plan_service):
    course_code = input("Which course do you want to remove from your plan? ")
    plan_service.delete_course(course_code)


def print_list(output_list):
    for row in output_list:
        print(row)

def matriculation_examination(plan_service):
    print("You want to compete with YTL?")


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
                import_courses(plan_service)
            case 4:
                print_list(plan_service.print_courses())
            case 5:
                plan_service.validate_plan()
            case 6:
                print_list(plan_service.print_stats())
            case 7:
               matriculation_examination(plan_service)
            case 10:
                print("exiting...")
                break
            case _:
                print("Command not found")


if __name__ == "__main__":
    main()
