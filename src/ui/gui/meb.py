import tkinter as tk
from tkinter import ttk

from config.meb_config import get_meb_names_and_codes_by_day, get_meb_names_and_codes

class MEB:
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root
        self._print_area = None
        self._valid_print_area = None

        self._options = get_meb_names_and_codes_by_day()
        self._meb_names_codes = get_meb_names_and_codes()

        title = ttk.Label(self._root, text="Matriculation examination")
        title.grid(column=0, row=0)

        self.print_meb_plan()

        add_button = ttk.Button(self._root, command=self.change_exams, text="Add exam")
        add_button.grid(column=0, row=2)

        validate_button = ttk.Button(self._root, command=self.validate_plan, text="Validate MEB plan")
        validate_button.grid(column=0, row=3)

    def print_meb_plan(self):
        if self._print_area:
            self._print_area.destroy()

        self._print_area = ttk.Frame(self._root)
        self._print_area.grid(column=0, row=1)

        meb_plan = self._plan_service.get_meb_plan()
        for i in range(1, 4):
            exams = " ".join(meb_plan[i])
            text = f"Examination period {i}: {exams}"
            label = ttk.Label(self._print_area, text=text)
            label.grid(column=0, row=i-1)

    def validate_plan(self):
        if self._valid_print_area:
            self._valid_print_area.destroy()

        self._valid_print_area = ttk.Frame(self._root)
        self._valid_print_area.grid(column=0, row=4)

        validation_status = self._plan_service.validate_meb()

        if validation_status:
            print(validation_status)
            for problem in validation_status:
                if "structure_problems" in problem.keys():
                    label = ttk.Label(self._valid_print_area, text=problem["structure_problems"])
                    label.grid(column=0, row=0)
        else:
            label = ttk.Label(self._valid_print_area, text="MEB plan OK!")
            label.grid(column=0, row=0)

    def save_exams(self, pop_up, values):
        for i in range(1, 4):
            for j in range(1, 9):
                exam_name = values[i][j].get()

                old_exam = self.get_current_exam(i, j)
                if old_exam:
                    old_exam_code = self._meb_names_codes[old_exam]
                    self._plan_service.remove_exam_meb(old_exam_code, i)

                if exam_name != "(none)":
                    exam_code = self._meb_names_codes[exam_name]
                    self._plan_service.add_exam_meb(exam_code, i)

        self.print_meb_plan()
        pop_up.destroy()

    def get_current_exam(self, period, day):
        old_meb_plan = self._plan_service.get_meb_plan()

        old_course = set(old_meb_plan[period]).intersection(set(self._options[day].values()))

        if old_course:
            return self._meb_names_codes[old_course.pop()]

        return None




    def change_exams(self):
        pop_up = tk.Toplevel(self._root)
        pop_up.geometry("750x250")

        values = {}

        day_str = {
            1: "mother tongue",
            2: "second national language",
            3: "long foreign language",
            4: "short foreign language",
            5: "mathemtaics",
            6: "nature sciences and humanities 1",
            7: "nature sciences and humanities 2",
            8: "sami as mother tongue"
        }

        meb_drop_downs = tk.Frame(pop_up)


        for k in range(1, 9):
            label = tk.Label(meb_drop_downs, text=day_str[k])
            label.grid(column=k, row=0)

        for i in range(1, 4):
            label = ttk.Label(meb_drop_downs, text=f"Examination period {i}")
            label.grid(column=0, row=i)

            values[i] = {}

            for j in range(1, 9):
                default_value = "(none)"
                old_course = self.get_current_exam(i, j)

                if old_course:
                    default_value = old_course

                values[i][j] = tk.StringVar()

                drop = ttk.OptionMenu(meb_drop_downs, values[i][j], default_value, *self._options[j].keys())
                drop.grid(column=j, row=i)


        meb_drop_downs.grid(column=0, row=0)

        button = tk.Button(pop_up, text= "Save", command=lambda: self.save_exams(pop_up, values))
        button.grid(column=0, row=1)
