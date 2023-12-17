from objects.plan import Plan
from objects.curriculum import Curriculum

from services.validation.special_validation_service import SpecialValidationService
from services.validation.validation_functions import ValidationFunctions


class ValidationService:
    """Luokka, joka vastaa opintosuunnitelman validioinnista.
    """

    def validate(self, plan: Plan, curriculum: Curriculum) -> list:
        """Validioi opintosuunnitelma

        Hyväksytyn tuloksen saa seuraavilla ehdoilla:
        - Opintopisteitä vähintään "minimum_credits"
        - Valtakunnallisia valinnaisia opintopisteitä 
          vähintään "minimum_national_voluntary_credits"
        - Kaikki pakolliset opintopisteet käyty

        Args:
            plan (Plan): Validioitava suunnitelma
            curriculum (Curriculum): Opetussunnitelma, jonka sääntöjä käyetään

        Returns:
            list: Validiointivirheet (tyhjä jos validiointi menee läpi)
        """
        validation_problems = []

        total_credits_status = self.__check_total_credits(
            plan, curriculum, validation_problems)
        self.__check_national_voluntary_credits(
            plan, curriculum, validation_problems)

        special_task_status = plan.return_config()["special_task"]

        if special_task_status and total_credits_status:
            special_validator = SpecialValidationService()
            special_plan_problems = special_validator.validate(
                plan, curriculum)

            if len(special_plan_problems) != 0:
                validation_problems.append({"name": "special_task_problems",
                                            "details": special_plan_problems})
            else:
                validation_problems = []

        else:
            self.__check_mandatory_credits(
                plan, curriculum, validation_problems)

        return validation_problems

    def __check_total_credits(self, plan: Plan,
                              curriculum: Curriculum,
                              validation_problems: list) -> bool:
        total_credit_rule = curriculum.return_rules()["minimum_credits"]
        total_credits = plan.get_total_credits_on_plan()

        if total_credits < total_credit_rule:
            validation_problems.append(
                {"name": "not_enough_credits", "details": total_credits})
            return False

        return True

    def __check_mandatory_credits(self, plan: Plan,
                                  curriculum: Curriculum,
                                  validation_problems: list) -> bool:
        validation_functions = ValidationFunctions()
        mandatory_credits_problems = {"full_credits": [], "half_credits": []}

        missing_credits = validation_functions.check_total_mandatory(
            plan, curriculum, mandatory_credits_problems)

        if missing_credits != 0:
            validation_problems.append({"name": "not_all_compulsory_credits",
                                        "details": mandatory_credits_problems["full_credits"]})

    def __check_national_voluntary_credits(self, plan: Plan,
                                           curriculum: Curriculum,
                                           validation_problems: list):
        voluntary_credit_rule = curriculum.return_rules(
        )["minimum_national_voluntary_credits"]
        voluntary_credits = plan.get_credits_by_criteria(
            mandatory=False, national=True)

        if voluntary_credits < voluntary_credit_rule:
            validation_problems.append({"name": "not_enough_national_voluntary_credits",
                                        "details": voluntary_credits})
