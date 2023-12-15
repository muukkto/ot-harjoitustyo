import re

import tkinter as tk
from tkinter import ttk

from config.meb_config import get_meb_names_and_codes_by_day, get_meb_names_and_codes, get_meb_days
from config.config import MAX_MEB_PERIODS, N_MEB_DAYS


class MEB:
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root
        self._print_area = None
        self._valid_print_area = None

        self._plan_config = None

        self._options = None
        self._meb_names_codes = None

        title = ttk.Label(self._root, text="Matriculation examination")
        title.grid(column=0, row=0)

        self.print_meb_plan()

        add_button = ttk.Button(
            self._root, command=self.change_exams, text="Update exams")
        add_button.grid(column=0, row=2)

        validate_button = ttk.Button(
            self._root, command=self.validate_plan, text="Validate MEB plan")
        validate_button.grid(column=0, row=3)

    def print_meb_plan(self):
        if self._print_area:
            self._print_area.destroy()

        self._print_area = ttk.Frame(self._root)
        self._print_area.grid(column=0, row=1)

        examination_periods = self._examination_period_prints()

        meb_plan = self._plan_service.get_meb_plan()
        for i in range(1, MAX_MEB_PERIODS+1):
            exams = " ".join(meb_plan[i])
            text = f"{examination_periods[i]}: {exams}"
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
                    label = ttk.Label(self._valid_print_area,
                                      text=problem["structure_problems"])
                    label.grid(column=0, row=0)
        else:
            label = ttk.Label(self._valid_print_area, text="MEB plan OK!")
            label.grid(column=0, row=0)

    def save_exams(self, pop_up, values):
        for i in range(1, MAX_MEB_PERIODS+1):
            for j in range(1, N_MEB_DAYS+1):
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

        old_course = set(old_meb_plan[period]).intersection(
            set(self._options[day].values()))

        if old_course:
            return self._meb_names_codes[old_course.pop()]

        return None

    def change_exams(self):
        pop_up = tk.Toplevel(self._root)
        pop_up.geometry("750x250")

        self._plan_config = self._plan_service.get_config()
        self._options = get_meb_names_and_codes_by_day(
            self._plan_config["meb_language"])
        self._meb_names_codes = get_meb_names_and_codes(
            self._plan_config["meb_language"])

        values = {}

        meb_drop_downs = tk.Frame(pop_up)

        examination_periods = self._examination_period_prints()

        for k in range(1, N_MEB_DAYS+1):
            label = tk.Label(meb_drop_downs, text=get_meb_days("en")[k])
            label.grid(column=k, row=0)

        for i in range(1, MAX_MEB_PERIODS+1):
            label = ttk.Label(meb_drop_downs, text=examination_periods[i])
            label.grid(column=0, row=i)

            values[i] = {}

            for j in range(1, 9):
                default_value = "(none)"
                old_course = self.get_current_exam(i, j)

                if old_course:
                    default_value = old_course

                values[i][j] = tk.StringVar()

                drop = ttk.OptionMenu(
                    meb_drop_downs, values[i][j], default_value, *self._options[j].keys())
                drop.grid(column=j, row=i)

        meb_drop_downs.grid(column=0, row=0)

        button = tk.Button(pop_up, text="Save",
                           command=lambda: self.save_exams(pop_up, values))
        button.grid(column=0, row=1)

    def _examination_period_prints(self):
        graduation_period = self._plan_service.get_config()["graduation_period"]

        if graduation_period:
            graduation_year = int(re.split(r"([SK])", graduation_period)[0])
            graduation_semester = re.split(r"([SK])", graduation_period)[1]

            meb_periods = {}

            for i in range(0, MAX_MEB_PERIODS):
                if graduation_semester == "S":
                    exam_semester = "S" if i % 2 == 0 else "K"
                    exam_year = graduation_year - (i // 2)
                else:
                    exam_semester = "K" if i % 2 == 0 else "S"
                    exam_year = graduation_year - ((i+1) // 2)

                meb_periods[MAX_MEB_PERIODS-i] = f"{exam_year}{exam_semester}"

            return meb_periods

        else:
            generic_periods = {}

            for i in range(1, MAX_MEB_PERIODS+1):
                generic_periods[i] = f"Examination period {i}"

            return generic_periods
