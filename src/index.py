from services.plan_service import PlanService

def print_commands():
    print("1: add course to your plan")
    print("2: delete course from your plan")
    print("3: print courses added to your plan")
    print("8: exit the program")

def main():
    plan_service = PlanService()

    while True:
        command = int(input("Choose command (0 for help): "))

        if command == 0:
            print_commands()
        elif command == 1:
            plan_service.add_course()
        elif command == 2:
            plan_service.delete_course()
        elif command == 3:
            plan_service.print_courses()
        elif command == 8:
            break
        else:
            print("Command not found")


if __name__ == "__main__":
    main()