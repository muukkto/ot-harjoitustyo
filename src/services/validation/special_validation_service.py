from objects.plan import Plan
from objects.curriculum import Curriculum

from services.validation.validation_functions import ValidationFunctions


class SpecialValidationService:
    """Luokka, joka vastaa opintosuunnitelman validioinnista 
       mikäli suunnitelma noudattaa eritysitehtävän tuntijakoa
    """

    def validate(self, plan: Plan, curriculum: Curriculum) -> list:
        """Validioi erityistehtväopintosuunnitelma

        Hyväksytyn tuloksen saa seuraavilla ehdoilla:
        - Erityistehtävä opintoja on vähintään "minimum_special_task_credits"
        - Jokaisesta oppiaineesta käyty vähintään puolet pakollisista opintopisteistä
        - Puuttuvia pakollisia opintopisteitä korkeintaan "maximum_excluded_credits_special_task"

        Args:
            plan (Plan): Validioitava suunnitelma
            curriculum (Curriculum): Opetussunnitelma, jonka sääntöjä käyetään

        Returns:
            list: Validiointivirheet (tyhjä jos validiointi menee läpi)
        """
        validation_problems = []

        special_task_credits_status = self.__check_special_task_credits(
            plan, curriculum)
        excluded_courses_status = self.__check_excluded_credits(
            plan, curriculum)

        validation_problems.extend(special_task_credits_status)
        validation_problems.extend(excluded_courses_status)

        return validation_problems

    def __check_special_task_credits(self, plan: Plan, curriculum: Curriculum) -> list:
        special_task_code = curriculum.return_rules()["special_task_code"]
        special_task_credits_rule = curriculum.return_rules()[
            "minimum_special_task_credits"]

        special_task_credits = plan.get_credits_by_criteria(
            mandatory=False, national=False, subject=special_task_code)

        if special_task_credits >= special_task_credits_rule:
            return []

        return [{"name": "not_enough_special_task_credits",
                 "details": special_task_credits}]

    def __check_excluded_credits(self, plan: Plan, curriculum: Curriculum) -> list:
        mandatory_courses_excluded_rule = curriculum.return_rules(
        )["maximum_excluded_credits_special_task"]

        validation_functions = ValidationFunctions()

        excluded_courses_problems = {"full_credits": [], "half_credits": []}
        excluded_credits = validation_functions.check_total_mandatory(
            plan, curriculum, excluded_courses_problems)

        if len(excluded_courses_problems["half_credits"]) == 0:
            if excluded_credits <= mandatory_courses_excluded_rule:
                return []

            return [{"name": "too_much_total_excluded_credits",
                     "details": excluded_credits}]

        return [{"name": "too_much_excluded_credits_per_subject",
                 "details": excluded_courses_problems["half_credits"]}]
