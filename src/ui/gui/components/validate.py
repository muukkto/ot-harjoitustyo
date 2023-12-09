from tkinter import ttk

class Validate:
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root
        self._print_area = None

        title = ttk.Label(self._root, text="Validation")
        title.grid(column=0, row=0)

        button = ttk.Button(self._root, command=self.print_validation, text="Validate plan")
        button.grid(column=0, row=1)

    def print_validation(self):
        if self._print_area:
            self._print_area.destroy()

        self._print_area = ttk.Frame(self._root)
        self._print_area.grid(column=0, row=2)

        validation_status = self._plan_service.validate_plan()

        if validation_status:
            for i, problem in enumerate(validation_status):
                label = ttk.Label(self._print_area, text=problem["name"])
                label.grid(column=0, row=i)
        else:
            label = ttk.Label(self._print_area, text="Plan OK!")
            label.grid(column=0, row=0)

