from tkinter import ttk
import tkinter as tk


class Statistics:
    """Komponentti joka vastaa tilastojen näyttämisestä graafisessa käyttöliittymässä
    
    Attributes:
        root: Juuriobjekti, jonka sisälle asetetaan kaikki Tkinter-objektit.
        plan_service: Suunnitelman hallinnasta vastaava luokka.
    """
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root
        self._print_area = None

        title = ttk.Label(self._root, text="Statistics")
        title.grid(column=0, row=0)

        self.print_stats()

    def print_stats(self):
        """Hakee suunnitelman tilastot ja esittää ne.
        """
        if self._print_area:
            self._print_area.destroy()

        stat_prints = {
            "total_credits": "Total credits",
            "mandatory_credits": "Mandatory credits",
            "national_voluntary_credits": "National voluntary credits",
            "local_voluntary_credits": "Local coluntary credits"
        }

        self._print_area = ttk.Frame(self._root)
        self._print_area.grid(column=0, row=1)

        stats = self._plan_service.get_stats()

        for i, (stat_code, stat_value) in enumerate(stats.items()):
            stat_title = ttk.Label(self._print_area, text=stat_prints[stat_code])
            stat_title.grid(column=0, row=i, sticky=tk.W)
            stat_info = ttk.Label(self._print_area, text=stat_value)
            stat_info.grid(column=1, row=i, sticky=tk.W)
