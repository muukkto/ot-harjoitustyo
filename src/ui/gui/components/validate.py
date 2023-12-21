from tkinter import ttk, messagebox


class Validate:
    def __init__(self, root, plan_service):
        self._plan_service = plan_service

        self._root = root

        title = ttk.Label(self._root, text="Validation")
        title.grid(column=0, row=0)

        button = ttk.Button(
            self._root, command=self.print_validation, text="Validate plan")
        button.grid(column=0, row=1)

    def subject_error_list(self, subject_problems):
        list_items = []
        for problem_subject in subject_problems:
            if problem_subject["name"] == "problem_with_simple_subjects":
                list_items.append(f"\tsubject: {problem_subject['details']}")
            elif problem_subject["name"] == "problem_with_group_subjects":
                list_items.append(f"\tsubject group: "
                                  f"{problem_subject['details'].replace('_', ' ')}")
            elif problem_subject["name"] == "problem_with_basket_subjects":
                list_items.append(f"\tsubject basket: "
                                  f"{problem_subject['details'].replace('_', ' ')}")

        if len(list_items) <= 5:
            return '\n'.join(list_items)
        else:
            return '\n'.join(list_items[0:5] + ["\t..."])

    def return_error_text(self, problem):
        if problem["name"] == "not_enough_credits":
            return f"Not enough credits. Minimum is 150 ects. You have {problem['details']} ects."
        elif problem["name"] == "not_enough_national_voluntary_credits":
            return f"Not enough national voluntary credits. Minimum is 20 ects. You have {problem['details']} ects."
        elif problem["name"] == "not_all_compulsory_credits":
            subject_problems = self.subject_error_list(problem["details"])

            return f"You haven't chosen all compulsory credits. You are missing credits in following subjects:\n{subject_problems}"
        elif problem["name"] == "special_task_problems":
            filter_1 = list(filter(
                lambda spec_problem: spec_problem["name"] == "not_enough_special_task_credits", problem["details"]))
            filter_2 = list(filter(
                lambda spec_problem: spec_problem["name"] == "too_much_total_excluded_credits", problem["details"]))
            filter_3 = list(filter(
                lambda spec_problem: spec_problem["name"] == "too_much_excluded_credits_per_subject", problem["details"]))

            if filter_1:
                return f"Not enough special task credits. Minimum is 24 ects. You have {filter_1[0]['details']} ects."
            if filter_2:
                return f"Too much excluded credits in total. Maximum is 16 ects. You lack {filter_2[0]['details']} ects."
            if filter_3:
                subject_problems = self.subject_error_list(
                    filter_3[0]["details"])

                return f"You haven't chosen atleast half of the compulsory credits in following subjects:\n{subject_problems}"

        return "Unknown problem in your plan!"

    def print_validation(self):
        validation_status = self._plan_service.validate_plan()

        if validation_status:
            error_message = []
            for problem in validation_status:
                error_message.append(self.return_error_text(problem))

            messagebox.showerror("Validation status", "\n".join(error_message))
        else:
            messagebox.showinfo("Validation status",
                                "Plan OK! You will graduate!")
