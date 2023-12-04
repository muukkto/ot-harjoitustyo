from ui.text_ui.print_commands import print_list

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

def plan_editor(plan_service):
    while True:
        print("1: add a new course\n2: remove a course\n0: main menu")
        match int(input("Choose commad: ")):
            case 1:
                add_course(plan_service)
            case 2:
                delete_course(plan_service)
            case 0:
                break
            case _:
                print("Command not found")

def config_editor(plan_service):
    while True:
        print("1: change plan to special task\n2: change plan to not special task\n3: print config\n0: main menu")
        match int(input("Choose commad: ")):
            case 1:
                plan_service.change_special_task_status(True)
            case 2:
                plan_service.change_special_task_status(False)
            case 3:
                print_list(plan_service.get_config())
            case 0:
                break
            case _:
                print("Command not found")
