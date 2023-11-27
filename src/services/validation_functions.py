class ValidationFunctions:
    def check_mandatory_credits_one_subject(self, plan, curriculum, subject):
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = plan.get_mandatory_credits_subject(subject)

        if curriculum_mandatory_credits / 2 > plan_mandatory_credits:
            return 9999

        return curriculum_mandatory_credits - plan_mandatory_credits

    def check_mandatory_credits_one_basket(self, plan, basket):
        plan_total_mandatory_credits = 0
        basket_rules = basket[1]

        for subject in basket_rules["subjects"]:
            ects_credits = plan.get_mandatory_credits_subject(subject)
            if ects_credits < basket_rules["minimum_compulsory_per_subject"]/2:
                return 9999

            plan_total_mandatory_credits += ects_credits

        return basket_rules["minimum_compulsory_total"] - plan_total_mandatory_credits

    def check_mandatory_credits_one_group(self, plan, curriculum, group):
        subject_list = curriculum.rules[group]
        least_exluded = 9999

        for subject in subject_list:
            subject_return = self.check_mandatory_credits_one_subject(
                plan, curriculum, subject)

            least_exluded = min(subject_return, least_exluded)

        return least_exluded

    def check_mandatory_all_subjects(self, plan, curriculum, excluded_creds, subj_problems):
        simple_subjects = curriculum.rules["national_mandatory_subjects"]

        for subject in simple_subjects:
            subject_return = self.check_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if subject_return > 1000:
                subj_problems.append(
                    {"name": "problem_with_simple_subjects", "details": subject})

            excluded_creds += subject_return

        return excluded_creds

    def check_mandatory_all_groups(self, plan, curriculum, excluded_credits, group_problems):
        group_subjects = [
            "mother_tongue",
            "second_national_language",
            "long_foreign_language",
            "maths",
            "worldview"
        ]

        for group in group_subjects:
            group_return = self.check_mandatory_credits_one_group(
                plan, curriculum, group)
            if group_return > 1000:
                group_problems.append(
                    {"name": "problem_with_group_subjects", "details": group})

            excluded_credits += group_return

        return excluded_credits

    def check_mandatory_all_baskets(self, plan, curriculum, excluded_credits, basket_problems):
        basket_subjects = curriculum.rules["basket_subjects"]

        for basket in basket_subjects.items():
            basket_return = self.check_mandatory_credits_one_basket(
                plan, basket)
            if basket_return > 1000:
                basket_problems.append(
                    {"name": "problem_with_basket_subjects", "details": basket[0]})

            excluded_credits += basket_return

        return excluded_credits

    def check_total_mandatory(self, plan, curriculum, mandatory_courses_problems):
        excluded_credits = 0

        excluded_credits = self.check_mandatory_all_subjects(
            plan, curriculum, excluded_credits, mandatory_courses_problems)
        excluded_credits = self.check_mandatory_all_groups(
            plan, curriculum, excluded_credits, mandatory_courses_problems)
        excluded_credits = self.check_mandatory_all_baskets(
            plan, curriculum, excluded_credits, mandatory_courses_problems)

        return excluded_credits
