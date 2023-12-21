import tkinter as tk
from tkinter import ttk

import time
from bidict import bidict


class Config:
    def __init__(self, root, plan_service, reload_meb_plan):
        self._plan_service = plan_service
        self._reload_meb_plan = reload_meb_plan

        self._root = root

        title = ttk.Label(self._root, text="Plan configuration")
        title.grid(column=0, row=0)

        edit_button = ttk.Button(
            self._root, command=self.edit_config, text="Edit plan config")
        edit_button.grid(column=0, row=2)

    def save_config(self, pop_up, variables):
        new_special_task = self.special_task_options_text_to_bool[variables["special_task"].get(
        )]
        new_meb_language = variables["meb_language"].get()
        new_period = variables["graduation_period"].get()

        self._plan_service.change_special_task_status(new_special_task)
        self._plan_service.change_meb_language(new_meb_language)
        self._plan_service.change_graduation_period(new_period)

        self._reload_meb_plan()

        pop_up.destroy()

    def edit_config(self):
        pop_up = tk.Toplevel(self._root)
        pop_up.geometry("200x100")

        config_frame = tk.Frame(pop_up)
        variables = {}

        special_task_options = {
            "normal plan": False,
            "special plan": True
        }

        meb_language_options = ["fi", "sv"]

        graduation_period_options = self._calculate_graduation_period_options()

        self.special_task_options_text_to_bool = bidict(special_task_options)
        self.special_task_options_bool_to_text = self.special_task_options_text_to_bool.inverse

        variables["special_task"] = tk.StringVar()
        variables["meb_language"] = tk.StringVar()
        variables["graduation_period"] = tk.StringVar()

        old_config = self._plan_service.get_config()

        old_special_task_status = old_config["special_task"]
        special_task_default_value = self.special_task_options_bool_to_text[
            old_special_task_status]

        old_meb_language = old_config["meb_language"]

        old_graduation_period = old_config["graduation_period"]

        special_task_drop = ttk.OptionMenu(
            config_frame, variables["special_task"], special_task_default_value, *self.special_task_options_text_to_bool.keys())

        meb_language_drop = ttk.OptionMenu(
            config_frame, variables["meb_language"], old_meb_language, *meb_language_options)

        graduation_period_drop = ttk.OptionMenu(
            config_frame, variables["graduation_period"], old_graduation_period, *graduation_period_options)

        config_frame.grid(column=0, row=0)
        special_task_drop.grid(column=0, row=0)
        meb_language_drop.grid(column=0, row=1)
        graduation_period_drop.grid(column=0, row=2)

        button = tk.Button(pop_up, text="Save",
                           command=lambda: self.save_config(pop_up, variables))
        button.grid(column=0, row=1)

    def _calculate_graduation_period_options(self) -> list:
        current_year = time.localtime()[0]
        current_month = time.localtime()[1]

        options = []

        for i in range(10):
            if current_month < 8:
                period = "K" if i % 2 == 0 else "S"
                year = current_year + i//2
            else:
                period = "S" if i % 2 == 0 else "K"
                year = current_year + (i+1)//2

            year_period = f"{year}{period}"

            options.append(year_period)

        return options
