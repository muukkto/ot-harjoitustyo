from ui.text_ui.print_commands import print_meb_plan


def meb_editor(plan_service):
    while True:
        print("1: add exam\n2: remove exam\n3: print meb plan\n0: main menu")
        match int(input("Choose command: ")):
            case 1:
                exam_code = input("Which exam do you want to add?")
                exam_period = int(
                    input("Which period do you want to write this exam?"))

                status = plan_service.add_exam_meb(exam_code, exam_period)

                if status:
                    print("Exam added succesfully!")
                else:
                    print("Couldn't add exam!")

            case 2:
                exam_code = input("Which exam do you want to remove?")
                exam_period = int(input("In which period is this exam?"))

                status = plan_service.remove_exam_meb(exam_code, exam_period)

                if status:
                    print("Exam removed succesfully!")
                else:
                    print("Couldn't remove exam!")
            case 3:
                print_meb_plan(plan_service)
            case 0:
                break
            case _:
                print("Command not found")
