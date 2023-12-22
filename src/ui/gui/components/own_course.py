import tkinter as tk
from tkinter import ttk

class OwnCourse:
    """Komponentti joka vastaa oman kurssin lisäämisestä graafisessa käyttöliittymässä
    
    Attributes:
        root: Juuriobjekti, jonka sisälle asetetaan kaikki Tkinter-objektit.
        plan_service: Suunnitelman hallinnasta vastaava luokka.
        reload_curriculum_tree: Funktio joka kutstutaan kun halutaan päivittää LOPS-puun näkymä.
        reload_stats: Funktio joka kutstutaan kun halutaan päivittää tilastojen näkymä.
    """
    def __init__(self, root, plan_service, reload_curriculum_tree, reload_stats):
        self._plan_service = plan_service

        self._root = root

        self._curriculum_tree_reload = reload_curriculum_tree
        self._stats_reload = reload_stats

        self._error_text = None
        self._error_label = None

        edit_button = ttk.Button(
            self._root, command=self._add_course, text="Add own course")
        edit_button.grid(column=0, row=0)

    def _show_error(self, message):
        self._error_text.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _save_course(self, code, name, ects, pop_up):
        if code:
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
        else:
            self._show_error("To add a course you need to give a course code!")


    def _add_course(self):
        pop_up = tk.Toplevel(self._root)
        pop_up.geometry("250x110")

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

        code_label.grid(column=0, row=1, sticky=tk.W)
        name_label.grid(column=0, row=2, sticky=tk.W)
        ects_label.grid(column=0, row=3, sticky=tk.W)
        code_input.grid(column=1, row=1)
        name_input.grid(column=1, row=2)
        ects_input.grid(column=1, row=3)

        button = tk.Button(pop_up, text="Save", command=lambda: self._save_course(
            code.get(), name.get(), ects.get(), pop_up))
        button.grid(column=0, row=4, columnspan=2)

        self._hide_error()
