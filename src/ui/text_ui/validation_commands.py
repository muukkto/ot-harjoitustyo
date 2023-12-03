from ui.text_ui.print_commands import print_list

def validation_handler(plan_service):
    print("1: validate study plan\n2: validate meb plan")
    match int(input("Choose command: ")):
        case 1:
            print_list(plan_service.validate_plan())
        case 2:
            print_list(plan_service.validate_meb())
        case _:
            print("Command not found")
