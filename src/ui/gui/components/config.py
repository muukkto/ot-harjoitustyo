import tkinter as tk
from tkinter import ttk

from bidict import bidict

class Config:
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root

        title = ttk.Label(self._root, text="Plan configuration")
        title.grid(column=0, row=0)

        edit_button = ttk.Button(self._root, command=self.edit_config, text="Edit plan config")
        edit_button.grid(column=0, row=2)

    def save_config(self, pop_up, variables):
        new_status = self.options_text_to_bool[variables["special_task"].get()]

        self._plan_service.change_special_task_status(new_status)

        print(self._plan_service.get_special_task_status())

        pop_up.destroy()


    def edit_config(self):
        pop_up = tk.Toplevel(self._root)
        pop_up.geometry("200x100")

        config_frame = tk.Frame(pop_up)
        variables = {}

        options = {
            "normal plan": False,
            "special plan": True
        }

        self.options_text_to_bool = bidict(options)
        self.options_bool_to_text = self.options_text_to_bool.inverse

        variables["special_task"] = tk.StringVar()

        old_status = self._plan_service.get_special_task_status()
        default_value = self.options_bool_to_text[old_status]

        drop = ttk.OptionMenu(config_frame, variables["special_task"], default_value, *self.options_text_to_bool.keys())

        config_frame.grid(column=0, row=0)
        drop.grid(column=0, row=0)

        button = tk.Button(pop_up, text= "Save", command=lambda: self.save_config(pop_up, variables))
        button.grid(column=0, row=1)
