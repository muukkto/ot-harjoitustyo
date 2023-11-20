class SpecialValidationService:
    def validate(self, plan, curriculum):
        validation_problems = []

        special_task_credits_status = self.check_special_task_credits(
            plan, curriculum)
        excluded_courses_status = self.check_excluded_credits(plan, curriculum)

        if not special_task_credits_status[0]:
            special_task_credits_on_plan = special_task_credits_status[1]
            validation_problems.append({"name": "not_enough_special_task_credits",
                                        "details": special_task_credits_on_plan})

        if not excluded_courses_status[0]:
            excluded_courses_problems = excluded_courses_status[1]
            validation_problems.append({"name": "too_much_excluded_courses",
                                        "details": excluded_courses_problems})

        return validation_problems

    def check_special_task_credits(self, plan, curriculum):
        special_task_code = curriculum.rules["special_task_code"]
        special_task_credits_rule = curriculum.rules["minimum_special_task_credits"]

        special_task_credits = plan.get_credits_by_criteria(
            mandatory=False, national=False, subject=special_task_code)

        return (special_task_credits >= special_task_credits_rule, special_task_credits)

    def check_half_mandatory_credits_one_subject(self, plan, curriculum, subject):
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = plan.get_mandatory_credits_subject(subject)

        if curriculum_mandatory_credits / 2 > plan_mandatory_credits:
            return (False, 9999)

        return (True, curriculum_mandatory_credits - plan_mandatory_credits)

    def check_half_mandatory_credits_one_basket(self, plan, basket):
        plan_total_mandatory_credits = 0
        basket_rules = basket[1]

        for subject in basket_rules["subjects"]:
            ects_credits = plan.get_mandatory_credits_subject(subject)
            if ects_credits < basket_rules["minimum_compulsory_per_subject"]/2:
                return (False, 9999)

            plan_total_mandatory_credits += ects_credits

        return (True, basket_rules["minimum_compulsory_total"] - plan_total_mandatory_credits)

    def check_half_mandatory_credits_one_group(self, plan, curriculum, group):
        subject_list = curriculum.rules[group]
        subject_status = False
        least_exluded = 9999

        for subject in subject_list:
            subject_return = self.check_half_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if subject_return[0]:
                subject_status = True
                least_exluded = min(subject_return[1], least_exluded)

        if subject_status:
            return (True, least_exluded)

        return (False, 9999)

    def check_half_mandatory_all_subjects(self, plan, curriculum, excluded_creds, subj_problems):
        simple_subjects = curriculum.rules["national_mandatory_subjects"]

        for subject in simple_subjects:
            subject_return = self.check_half_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if not subject_return[0]:
                subj_problems.append(
                    {"name": "problem_with_simple_subjects", "details": subject})

            excluded_creds += subject_return[1]

        return excluded_creds
    def check_half_mandatory_all_groups(self, plan, curriculum, excluded_credits, group_problems):
        group_subjects = [
            "mother_tongue",
            "second_national_language",
            "long_foreign_language",
            "maths",
            "worldview"
        ]

        for group in group_subjects:
            group_return = self.check_half_mandatory_credits_one_group(
                plan, curriculum, group)
            if not group_return[0]:
                group_problems.append(
                    {"name": "problem_with_group_subjects", "details": group})

            excluded_credits += group_return[1]

        return excluded_credits

    def check_half_mandatory_all_baskets(self, plan, curriculum, excluded_credits, basket_problems):
        basket_subjects = curriculum.rules["basket_subjects"]

        for basket in basket_subjects.items():
            basket_return = self.check_half_mandatory_credits_one_basket(
                plan, basket)
            if not basket_return[0]:
                basket_problems.append(
                    {"name": "problem_with_basket_subjects", "details": basket[0]})

            excluded_credits += basket_return[1]

        return excluded_credits

    def check_excluded_credits(self, plan, curriculum):
        mandatory_courses_excluded_rule = curriculum.rules["maximum_excluded_credits_special_task"]

        excluded_courses_problems = []
        excluded_credits = 0

        excluded_credits = self.check_half_mandatory_all_subjects(
            plan, curriculum, excluded_credits, excluded_courses_problems)
        excluded_credits = self.check_half_mandatory_all_groups(
            plan, curriculum, excluded_credits, excluded_courses_problems)
        excluded_credits = self.check_half_mandatory_all_baskets(
            plan, curriculum, excluded_credits, excluded_courses_problems)

        if len(excluded_courses_problems) == 0:
            if excluded_credits <= mandatory_courses_excluded_rule:
                return (True, "")

            excluded_courses_problems.append("too_much_excluded_courses")

        return (False, excluded_courses_problems)
