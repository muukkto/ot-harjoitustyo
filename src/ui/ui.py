import tkinter as tk
from tkinter import ttk

from services.plan_service import PlanService



class UI:
    def __init__(self, root):
        self._root = root
        self._plan_service = PlanService()

    def change_status(self, event):
        course_code = event.widget.cget("text")
        course_status = self._plan_service.get_course_status(course_code)

        if course_status:
            self._plan_service.delete_course(course_code)
            event.widget["bg"] = event.widget.master["bg"]
        else:
            self._plan_service.add_course(course_code)
            event.widget["bg"]="grey"

    def course(self, code, master_frame, information):
        if information["national"]:
            if information["mandatory"]:
                bg = "blue"
            else:
                bg = "red"
        else:
            bg = "white"

        course_frame = tk.Frame(master_frame, bg=bg)

        course_status = self._plan_service.get_course_status(code)
        if course_status:
            label = tk.Label(master=course_frame, text=code, bg="grey")
        else:
            label = tk.Label(master=course_frame, text=code, bg=bg)

        label.grid(row=0, column=0)

        label.bind('<Button-1>', self.change_status)

        return course_frame

    def start(self):
        container = ttk.Frame(self._root)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        curriculum_frame = ttk.Frame(canvas)

        curriculum_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=curriculum_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        curriculum = self._plan_service.get_curriculum_tree()

        for i, (subject, data) in enumerate(curriculum.items()):
            subject_frame = tk.Frame(master=curriculum_frame)
            
            subject_label = tk.Label(master=subject_frame, text=subject)

            courses = data["courses"]
            courses_frame = tk.Frame(master=subject_frame)

            for j, (code, information) in enumerate(courses.items()):
                courses_obj = self.course(code, courses_frame, information)
                courses_obj.grid(row=1, column=j)


            subject_label.grid(row=0, column=0, sticky=tk.W)
            courses_frame.grid(row=1, column=0)

            subject_frame.grid(row=i, column=0, sticky=tk.W)


        container.grid(column=0, row=0, sticky=tk.N+tk.W+tk.S)
        canvas.grid(column=0, row=0, sticky=tk.N+tk.W+tk.S)
        scrollbar.grid(column=1, row=0, sticky=tk.N+tk.E+tk.S)

        self._root.rowconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, minsize=600)
        canvas.rowconfigure(0, weight=1)

        #container.pack()
        #canvas.pack(side="left", fill="both", expand=True)
        #scrollbar.pack(side="right", fill="y")
