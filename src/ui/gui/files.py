from tkinter import ttk, filedialog

from services.file_service import FileService

class Files:
    def __init__(self, root, plan_service, curriculum_tree, meb, stats):
        self._plan_service = plan_service
        self._curriculum_tree = curriculum_tree
        self._meb = meb
        self._stats = stats

        self._root = root

        title = ttk.Label(self._root, text="Import/export plan")
        title.grid(column=0, row=0)

        button_import = ttk.Button(self._root, command=self._import_json, text="import plan (JSON)")
        button_import.grid(column=0, row=1)

        button_export = ttk.Button(self._root, command=self._export_json, text="export plan (JSON)")
        button_export.grid(column=0, row=2)

    def _import_json(self):
        file_service = FileService()

        filetypes = (('Plan file (*.json)', '*.json'),)
        file_path = filedialog.askopenfilename(filetypes=filetypes)

        file_service.import_plan_from_json(self._plan_service, file_path)

        self._curriculum_tree.init_curriculum_tree()
        self._meb.print_meb_plan()
        self._stats.print_stats()

    def _export_json(self):
        file_service = FileService()

        filetypes = (('Plan file (*.json)', '*.json'),)
        file_path = filedialog.asksaveasfilename(filetypes=filetypes)

        file_service.export_plan_to_json(self._plan_service, file_path)
