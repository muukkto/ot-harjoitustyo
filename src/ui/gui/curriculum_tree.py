import tkinter as tk

class CurriculumTree:
    def __init__(self, root, plan_service, stats):
        self._root = root
        self._print_area = None
        self._plan_service = plan_service
        self._stats = stats

    def init_curriculum_tree(self):
        if self._print_area:
            self._print_area.destroy()

        self._print_area = tk.Frame(self._root)

        curriculum = self._plan_service.get_curriculum_tree()
        curriculum_courses_frame = tk.Frame(self._print_area)

        for i, (subject, data) in enumerate(curriculum.items()):
            self.subject(curriculum_courses_frame, i, subject, data)

        curriculum_courses_frame.grid(column=0, row=0)


        own_courses_frame = tk.Frame(self._print_area)

        own_courses_label = tk.Label(master=own_courses_frame, text="Own courses")
        own_courses_label.grid(row=0, column=0, sticky=tk.W)

        own_courses = self._plan_service.get_own_courses()
        for i, course in enumerate(own_courses):
            gui_block = self.own_course(course, own_courses_frame)
            gui_block.grid(column=i, row=1)

        own_courses_frame.grid(row=1,column=0, sticky=tk.W)


        self._print_area.grid(column=0, row=0)

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

    def remove_own_course(self, event):
        self._plan_service.delete_course(event.widget["text"])
        self.init_curriculum_tree()

        self._stats.print_stats()

    def own_course(self, course_object, master_frame):
        bg = "grey"

        course_frame = tk.Frame(master_frame, bg=bg, highlightbackground="black", highlightthickness=1)

        title_label = tk.Label(course_frame, text=str(course_object), bg=bg)
        ects_label = tk.Label(course_frame, text=course_object.get_ects(), bg=bg)

        title_label.grid(column=0, row=0)
        ects_label.grid(column=0, row=1)

        title_label.bind('<Button-1>', self.remove_own_course)

        return course_frame


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
