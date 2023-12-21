import tkinter as tk
from tkinter import ttk

class OwnCourse:
    def __init__(self, root, plan_service, curriculum_tree, stats):
        self._plan_service = plan_service

        self._root = root

        self._curriculum_tree_reload = curriculum_tree
        self._stats_reload = stats

        self._error_text = None
        self._error_label = None

        edit_button = ttk.Button(
            self._root, command=self.add_course, text="Add own course")
        edit_button.grid(column=0, row=0)

    def _show_error(self, message):
        self._error_text.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def save_course(self, code, name, ects, pop_up):
        try:
            if self._plan_service.add_course(code, name, int(ects), in_cur=False):
                pop_up.destroy()

                self._curriculum_tree_reload()
                self._stats_reload()
            else:
                self._show_error(
                    "Cannot add own course with same subject code as in curriculum!")
        except ValueError:
            self._show_error("Couldn't add own course, check your input!")

    def add_course(self):
        pop_up = tk.Toplevel(self._root)
        pop_up.geometry("400x250")

        code = tk.StringVar()
        name = tk.StringVar()
        ects = tk.StringVar()

        code_label = tk.Label(pop_up, text="Course code")
        name_label = tk.Label(pop_up, text="Course name")
        ects_label = tk.Label(pop_up, text="Credits")

        code_input = tk.Entry(pop_up, textvariable=code)
        name_input = tk.Entry(pop_up, textvariable=name)
        ects_input = tk.Entry(pop_up, textvariable=ects)

        self._error_text = tk.StringVar(pop_up)
        self._error_label = ttk.Label(
            master=pop_up,
            textvariable=self._error_text,
            foreground="red"
        )

        self._error_label.grid(row=0, column=0, columnspan=2)

        code_label.grid(column=0, row=1)
        name_label.grid(column=0, row=2)
        ects_label.grid(column=0, row=3)
        code_input.grid(column=1, row=1)
        name_input.grid(column=1, row=2)
        ects_input.grid(column=1, row=3)

        button = tk.Button(pop_up, text="Save", command=lambda: self.save_course(
            code.get(), name.get(), ects.get(), pop_up))
        button.grid(column=0, row=4, columnspan=2)

        self._hide_error()
