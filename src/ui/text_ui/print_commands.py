def print_list(output_list):
    for row in output_list:
        print(row)

def print_meb_plan(plan_service):
    meb_plan = plan_service.get_meb_plan()

    print("Current matriculation examination plan")

    for i in range(1, 4):
        print(f"Exam period {i}: {" ".join(meb_plan[i])}")

def print_handler(plan_service):
    print("1: print stats\n2: print courses on plan\n3: print exams on meb plan")
    match int(input("Choose command: ")):
        case 1:
            print_list(plan_service.get_stats())
        case 2:
            print_list(plan_service.get_courses())
        case 3:
            print_meb_plan(plan_service)
        case _:
            print("Command not found")
