from tkinter import ttk
import tkinter as tk


class Statistics:
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root
        self._print_area = None

        title = ttk.Label(self._root, text="Statistics")
        title.grid(column=0, row=0)

        self.print_stats()

    def print_stats(self):
        if self._print_area:
            self._print_area.destroy()

        self._print_area = ttk.Frame(self._root)
        self._print_area.grid(column=0, row=1)

        stats = self._plan_service.get_stats()
        for i, (stat_name, stat_value) in enumerate(stats.items()):
            stat_title = ttk.Label(self._print_area, text=stat_name)
            stat_title.grid(column=0, row=i, sticky=tk.W)
            stat_info = ttk.Label(self._print_area, text=stat_value)
            stat_info.grid(column=1, row=i, sticky=tk.W)
