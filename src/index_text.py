from services.plan_service import PlanService
from services.user_service import UserService

from ui.text_ui.plan_commands import plan_editor, config_editor
from ui.text_ui.meb_commands import meb_editor

from ui.text_ui.file_commands import file_handler
from ui.text_ui.validation_commands import validation_handler
from ui.text_ui.print_commands import print_handler


user_service = UserService()
plan_service = PlanService(user_service)


def print_commands():
    print("1: modify your plan")
    print("2: update matriculation examination plan")
    print("3: import plan from file")
    print("4: validate plan")
    print("5: print stats, courses or exams")

    print("9: change plan config")
    print("10: exit the program")


def main_page():
    while True:
        match int(input("Choose command (0 for help): ")):
            case 0:
                print_commands()
            case 1:
                plan_editor(plan_service)
            case 2:
                meb_editor(plan_service)
            case 3:
                file_handler(plan_service)
            case 4:
                validation_handler(plan_service)
            case 5:
                print_handler(plan_service)

            case 9:
                config_editor(plan_service)
            case 10:
                print("exiting...")
                break
            case _:
                print("Command not found")


def main():
    username = input("Choose username: ")

    if user_service.login(username):
        plan_service.read_plan_for_user()
    else:
        new_username = input("User not found\nCreate a new user: ")
        user_service.create_user(new_username)
        plan_service.create_empty_plan_for_user()

    main_page()


if __name__ == "__main__":
    main()
