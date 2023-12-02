import tkinter as tk
from tkinter import ttk

class CurriculumTree:
    def __init__(self, root, plan_service, stats):
        self._plan_service = plan_service
        self._stats = stats

        curriculum = self._plan_service.get_curriculum_tree()

        for i, (subject, data) in enumerate(curriculum.items()):
            self.subject(root, i, subject, data)

    def change_status(self, event):
        course_code = event.widget.cget("text")
        course_status = self._plan_service.get_course_status(course_code)

        if course_status:
            self._plan_service.delete_course(course_code)
            event.widget["bg"] = event.widget.master["bg"]
        else:
            self._plan_service.add_course(course_code)
            event.widget["bg"]="grey"

        self._stats.print_stats()


    def course(self, code, master_frame, information):
        if information["national"]:
            if information["mandatory"]:
                bg = "blue"
            else:
                bg = "red"
        else:
            bg = "white"

        course_frame = tk.Frame(master_frame, bg=bg, highlightbackground="black", highlightthickness=1)

        course_status = self._plan_service.get_course_status(code)
        if course_status:
            label = tk.Label(master=course_frame, text=code, bg="grey")
        else:
            label = tk.Label(master=course_frame, text=code, bg=bg)

        label.grid(row=0, column=0)

        label.bind('<Button-1>', self.change_status)

        return course_frame

    def subject(self, master_frame, index, subject, data):
        subject_frame = tk.Frame(master=master_frame)

        subject_label = tk.Label(master=subject_frame, text=subject)

        courses = data["courses"]
        courses_frame = tk.Frame(master=subject_frame)

        for j, (code, information) in enumerate(courses.items()):
            courses_obj = self.course(code, courses_frame, information)
            courses_obj.grid(row=1, column=j)


        subject_label.grid(row=0, column=0, sticky=tk.W)
        courses_frame.grid(row=1, column=0)

        subject_frame.grid(row=index, column=0, sticky=tk.W)