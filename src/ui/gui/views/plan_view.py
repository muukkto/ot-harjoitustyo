import tkinter as tk
from tkinter import ttk

from ui.gui.components.curriculum_tree import CurriculumTree
from ui.gui.components.stats import Statistics
from ui.gui.components.validate import Validate
from ui.gui.components.meb import MEB
from ui.gui.components.config import Config
from ui.gui.components.files import Files
from ui.gui.components.own_course import OwnCourse


class PlanView:
    def __init__(self, root, plan_service, user_service, login_view):
        self._root = root
        self._main_frame = ttk.Frame(self._root)
        self._plan_service = plan_service
        self._user_service = user_service
        self._login_view = login_view
        self._stats = None
        self._curriculum_tree = None
        self._meb = None

        self._main_frame.grid(row=0, column=0, sticky='ns')
        self._main_frame.rowconfigure(0, weight=1)

        self.start()

    def destroy(self):
        self._main_frame.destroy()

    def _reload_curriculum_tree(self):
        self._curriculum_tree.init_curriculum_tree()

    def _reload_meb_plan(self):
        self._meb.print_meb_plan()

    def _reload_stats(self):
        self._stats.print_stats()

    def _create_frame(self, root, row_index, column_index):
        frame = ttk.Frame(root)
        frame.grid(row=row_index, column=column_index)
        return frame

    def _handle_logout(self):
        self._user_service.logout()
        self._login_view()

    def start(self):
        self._curriculum_container()

        container = ttk.Frame(self._main_frame)
        container.grid(column=1, row=0, sticky=tk.N+tk.E+tk.S)

        stats_frame = self._create_frame(container, 0, 0)
        validate_frame = self._create_frame(container, 1, 0)
        meb_frame = self._create_frame(container, 0, 1)
        config_frame = self._create_frame(container, 1, 1)
        files_frame = self._create_frame(container, 2, 1)
        own_course_frame = self._create_frame(container, 2, 0)

        self._stats = Statistics(stats_frame, self._plan_service)
        Validate(validate_frame, self._plan_service)
        self._meb = MEB(meb_frame, self._plan_service)
        Config(config_frame, self._plan_service, self._reload_meb_plan)
        Files(files_frame, self._plan_service,
              self._reload_curriculum_tree,
              self._reload_meb_plan,
              self._reload_stats)
        OwnCourse(own_course_frame, self._plan_service,
                  self._reload_curriculum_tree,
                  self._reload_stats)

        logout_button = ttk.Button(
            container, text="logout", command=self._handle_logout)
        logout_button.grid(column=0, row=4, columnspan=2)

    def _curriculum_container(self):
        container = ttk.Frame(self._main_frame)
        canvas = tk.Canvas(container)
        scrollbar_v = ttk.Scrollbar(
            container, orient="vertical", command=canvas.yview)
        scrollbar_h = ttk.Scrollbar(
            container, orient="horizontal", command=canvas.xview)
        curriculum_frame = ttk.Frame(canvas)

        curriculum_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=curriculum_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_v.set)
        canvas.configure(xscrollcommand=scrollbar_h.set)

        self._curriculum_tree = CurriculumTree(curriculum_frame, self._plan_service,
                                               self._reload_stats)
        self._curriculum_tree.init_curriculum_tree()

        container.grid(column=0, row=0, sticky=tk.N+tk.W+tk.S+tk.E)
        canvas.grid(column=0, row=0, sticky=tk.N+tk.W+tk.S+tk.E)
        scrollbar_v.grid(column=1, row=0, sticky=tk.N+tk.E+tk.S)
        scrollbar_h.grid(column=0, row=1, sticky=tk.W+tk.E+tk.S)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, minsize=600)
        canvas.rowconfigure(0, weight=1)
        curriculum_frame.rowconfigure(0, weight=1)
