from tkinter import ttk

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

        stats = self._plan_service.print_stats()
        for i, stat in enumerate(stats):
            label = ttk.Label(self._print_area, text=stat)
            label.grid(column=0, row=i)
