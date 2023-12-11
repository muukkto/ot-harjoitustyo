from objects.plan import Plan
from objects.curriculum import Curriculum

class ValidationFunctions:
    """Luokkien ValidationService ja SpecialValidationService yhteiset funktiot
    """
    def __check_mandatory_credits_one_subject(self, plan: Plan, curriculum: Curriculum, subject: str) -> int:
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = plan.get_mandatory_credits_subject(subject)

        if curriculum_mandatory_credits / 2 > plan_mandatory_credits:
            return 9999

        return curriculum_mandatory_credits - plan_mandatory_credits

    def __check_mandatory_credits_one_basket(self, plan: Plan, basket: dict) -> int:
        plan_total_mandatory_credits = 0
        basket_rules = basket[1]

        for subject in basket_rules["subjects"]:
            ects_credits = plan.get_mandatory_credits_subject(subject)
            if ects_credits < basket_rules["minimum_compulsory_per_subject"]/2:
                return 9999

            plan_total_mandatory_credits += ects_credits

        return basket_rules["minimum_compulsory_total"] - plan_total_mandatory_credits

    def __check_mandatory_credits_one_group(self, plan: Plan, curriculum: Curriculum, group: str) -> int:
        subject_list = curriculum.return_rules()[group]
        least_exluded = 9999

        for subject in subject_list:
            subject_return = self.__check_mandatory_credits_one_subject(
                plan, curriculum, subject)

            least_exluded = min(subject_return, least_exluded)

        return least_exluded

    def __check_mandatory_all_subjects(self, plan: Plan, curriculum: Curriculum, excluded_creds: int, subj_problems: list) -> int:
        simple_subjects = curriculum.return_rules()[
            "national_mandatory_subjects"]

        for subject in simple_subjects:
            subject_return = self.__check_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if subject_return > 1000:
                subj_problems.append(
                    {"name": "problem_with_simple_subjects", "details": subject})

            excluded_creds += subject_return

        return excluded_creds

    def __check_mandatory_all_groups(self, plan: Plan, curriculum: Curriculum, excluded_credits: int, group_problems: list) -> int:
        group_subjects = [
            "mother_tongue",
            "second_national_language",
            "long_foreign_language",
            "maths",
            "worldview"
        ]

        for group in group_subjects:
            group_return = self.__check_mandatory_credits_one_group(
                plan, curriculum, group)
            if group_return > 1000:
                group_problems.append(
                    {"name": "problem_with_group_subjects", "details": group})

            excluded_credits += group_return

        return excluded_credits

    def __check_mandatory_all_baskets(self, plan: Plan, curriculum: Curriculum, excluded_credits: int, basket_problems: list) -> int:
        basket_subjects = curriculum.return_rules()["basket_subjects"]

        for basket in basket_subjects.items():
            basket_return = self.__check_mandatory_credits_one_basket(
                plan, basket)
            if basket_return > 1000:
                basket_problems.append(
                    {"name": "problem_with_basket_subjects", "details": basket[0]})

            excluded_credits += basket_return

        return excluded_credits

    def check_total_mandatory(self, plan: Plan, curriculum: Curriculum, mandatory_courses_problems: list) -> int:
        excluded_credits = 0

        excluded_credits = self.__check_mandatory_all_subjects(
            plan, curriculum, excluded_credits, mandatory_courses_problems)
        excluded_credits = self.__check_mandatory_all_groups(
            plan, curriculum, excluded_credits, mandatory_courses_problems)
        excluded_credits = self.__check_mandatory_all_baskets(
            plan, curriculum, excluded_credits, mandatory_courses_problems)

        return excluded_credits
