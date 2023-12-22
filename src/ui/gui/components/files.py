from tkinter import ttk, filedialog, messagebox

from services.file_service import export_plan_to_json, import_plan_from_json


class Files:
    """Komponentti joka vastaa tiedostojen lataamisesta ja tallentamisesta graafisessa käyttöliittymässä
    
    Attributes:
        root: Juuriobjekti, jonka sisälle asetetaan kaikki Tkinter-objektit.
        plan_service: Suunnitelman hallinnasta vastaava luokka.
        reload_curriculum_tree: Funktio joka kutstutaan kun halutaan päivittää LOPS-puun näkymä.
        reload_meb: Funktio joka kutstutaan kun halutaan päivittää YO-suunnitelman näkymä.
        reload_stats: Funktio joka kutstutaan kun halutaan päivittää tilastojen näkymä.
    """
    def __init__(self, root, plan_service, reload_curriculum_tree, reload_meb, reload_stats):
        self._plan_service = plan_service
        self._curriculum_tree_reload = reload_curriculum_tree
        self._meb_reload = reload_meb
        self._stats_reload = reload_stats

        self._root = root

        title = ttk.Label(self._root, text="Import/export plan")
        title.grid(column=0, row=0)

        button_import = ttk.Button(
            self._root, command=self._import_json, text="import plan (JSON)")
        button_import.grid(column=0, row=1)

        button_export = ttk.Button(
            self._root, command=self._export_json, text="export plan (JSON)")
        button_export.grid(column=0, row=2)

    def _import_json(self):
        filetypes = (('Plan file (*.json)', '*.json'),)
        file_path = filedialog.askopenfilename(filetypes=filetypes)

        try:
            plan_dict = import_plan_from_json(file_path)

            if plan_dict:
                self._plan_service.import_study_plan(plan_dict)

                self._curriculum_tree_reload()
                self._meb_reload()
                self._stats_reload()
            else:
                messagebox.showerror(
                    "Invalid plan file",  "Error: imported file is invalid")

        except FileNotFoundError:
            messagebox.showerror(
                "File not found",  "Error: file path is invalid")

    def _export_json(self):
        filetypes = (('Plan file (*.json)', '*.json'),)
        file_path = filedialog.asksaveasfilename(filetypes=filetypes)

        try:
            plan_dict = self._plan_service.get_study_plan()
            export_plan_to_json(plan_dict, file_path)
        except FileNotFoundError:
            messagebox.showerror(
                "File not found",  "Error: file path is invalid")
