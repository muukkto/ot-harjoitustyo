from tkinter import filedialog as fd

from services.file_service import import_plan_from_json, export_plan_to_json


def import_plan_json(plan_service):
    filetypes = (('Plan file (*.json)', '*.json'),)
    file_path = fd.askopenfilename(filetypes=filetypes)

    status = import_plan_from_json(plan_service, file_path)

    if status:
        print("Plan imported succesfully!")
    else:
        print("Plan couldn't be imported!")


def export_plan_json(plan_service):
    filetypes = (('Plan file (*.json)', '*.json'),)
    file_path = fd.asksaveasfilename(filetypes=filetypes)

    export_plan_to_json(plan_service, file_path)


def file_handler(plan_service):
    while True:
        print("1: import plan (JSON)\n2: export plan (JSON)\n0: main menu")
        match int(input("Choose command: ")):
            case 1:
                import_plan_json(plan_service)
            case 2:
                export_plan_json(plan_service)
            case 0:
                break
            case _:
                print("Command not found")
