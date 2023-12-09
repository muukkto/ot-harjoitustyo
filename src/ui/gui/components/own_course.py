import tkinter as tk
from tkinter import ttk

from bidict import bidict

class OwnCourse:
    def __init__(self, root, plan_service, curriculum_tree, stats):
        self._plan_service = plan_service

        self._root = root

        self._curriculum_tree_reload = curriculum_tree
        self._stats_reload = stats

        edit_button = ttk.Button(self._root, command=self.add_course, text="Add own course")
        edit_button.grid(column=0, row=0)

    def save_course(self, code, name, ects, pop_up):
        self._plan_service.add_course(code, name, int(ects), in_cur=False)
        pop_up.destroy()
        
        self._curriculum_tree_reload()
        self._stats_reload()

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

        code_label.grid(column=0, row=0)
        name_label.grid(column=0, row=1)
        ects_label.grid(column=0, row=2)
        code_input.grid(column=1, row=0)
        name_input.grid(column=1, row=1)
        ects_input.grid(column=1, row=2)

        button = tk.Button(pop_up, text= "Save", command=lambda: self.save_course(code.get(), name.get(), ects.get(), pop_up))
        button.grid(column=0, row=3, columnspan=2)
