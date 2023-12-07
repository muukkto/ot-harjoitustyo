import tkinter as tk
from tkinter import ttk

from services.plan_service import PlanService

from ui.gui.curriculum_tree import CurriculumTree
from ui.gui.stats import Statistics
from ui.gui.validate import Validate
from ui.gui.meb import MEB
from ui.gui.config import Config
from ui.gui.files import Files
from ui.gui.own_course import OwnCourse


class UI:
    def __init__(self, root):
        self._root = root
        self._plan_service = PlanService()
        self._stats = None
        self._curriculum_tree = None
        self._meb = None

    def start(self):
        container = ttk.Frame(self._root)
        container.grid(column=1, row=0, sticky=tk.N+tk.E+tk.S)

        stats_frame = ttk.Frame(container)
        validate_frame = ttk.Frame(container)
        meb_frame = ttk.Frame(container)
        config_frame = ttk.Frame(container)
        files_frame = ttk.Frame(container)
        own_course_frame = ttk.Frame(container)

        stats_frame.grid(column=0, row=0)
        validate_frame.grid(column=0, row=1)
        meb_frame.grid(column=1, row=0)
        config_frame.grid(column=1, row=1)
        files_frame.grid(column=1, row=2)
        own_course_frame.grid(column=0, row=2)

        self._stats = Statistics(stats_frame, self._plan_service)
        self._meb = MEB(meb_frame, self._plan_service)

        self.curriculum_container()

        Validate(validate_frame, self._plan_service)
        Config(config_frame, self._plan_service)
        Files(files_frame, self._plan_service, self._curriculum_tree, self._meb, self._stats)
        OwnCourse(own_course_frame, self._plan_service, self._curriculum_tree, self._stats)

    def curriculum_container(self):
        container = ttk.Frame(self._root)
        canvas = tk.Canvas(container)
        scrollbar_v = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar_h = ttk.Scrollbar(container, orient="horizontal", command=canvas.xview)
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

        self._curriculum_tree = CurriculumTree(curriculum_frame, self._plan_service, self._stats)
        self._curriculum_tree.init_curriculum_tree()

        container.grid(column=0, row=0, sticky=tk.N+tk.W+tk.S+tk.E)
        canvas.grid(column=0, row=0, sticky=tk.N+tk.W+tk.S+tk.E)
        scrollbar_v.grid(column=1, row=0, sticky=tk.N+tk.E+tk.S)
        scrollbar_h.grid(column=0, row=1, sticky=tk.W+tk.E+tk.S)

        self._root.rowconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, minsize=600)
        canvas.rowconfigure(0, weight=1)
