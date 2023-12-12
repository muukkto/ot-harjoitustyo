from tkinter import ttk, filedialog

from services.file_service import export_plan_to_json, import_plan_from_json


class Files:
    def __init__(self, root, plan_service, curriculum_tree, meb, stats):
        self._plan_service = plan_service
        self._curriculum_tree_reload = curriculum_tree
        self._meb_reload = meb
        self._stats_reload = stats

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

        plan_dict = import_plan_from_json(file_path)
        self._plan_service.import_study_plan(plan_dict)

        self._curriculum_tree_reload()
        self._meb_reload()
        self._stats_reload()

    def _export_json(self):
        filetypes = (('Plan file (*.json)', '*.json'),)
        file_path = filedialog.asksaveasfilename(filetypes=filetypes)

        plan_dict = self._plan_service.get_study_plan()
        export_plan_to_json(plan_dict, file_path)
