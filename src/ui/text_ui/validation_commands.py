from ui.text_ui.print_commands import print_list


def validation_handler(plan_service):
    while True:
        print("1: validate study plan\n2: validate meb plan\n0: main menu")
        match int(input("Choose command: ")):
            case 1:
                print_list(plan_service.validate_plan())
            case 2:
                print_list(plan_service.validate_meb())
            case 0:
                break
            case _:
                print("Command not found")
