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
    print("1: add a new course\n2: remove a course")
    match int(input("Choose commad: ")):
        case 1:
            add_course(plan_service)
        case 2:
            delete_course(plan_service)
        case _:
            print("Command not found")

def config_editor(plan_service):
    print("CONFIG")
