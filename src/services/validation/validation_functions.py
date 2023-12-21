from objects.plan import Plan
from objects.curriculum import Curriculum


class ValidationFunctions:
    """Luokkien ValidationService ja SpecialValidationService yhteiset funktiot
    """

    def __check_mandatory_credits_one_subject(self, plan: Plan,
                                              curriculum: Curriculum,
                                              subject: str) -> int:
        curriculum_mandatory_credits = curriculum.get_mandatory_credits_subject(
            subject)
        plan_mandatory_credits = plan.get_mandatory_credits_subject(subject)

        if curriculum_mandatory_credits / 2 > plan_mandatory_credits:
            return 9999

        return curriculum_mandatory_credits - plan_mandatory_credits

    def __check_mandatory_credits_one_basket(self, plan: Plan, basket: dict) -> int:
        plan_total_mandatory_credits = 0

        for subject in basket["subjects"]:
            ects_credits = plan.get_mandatory_credits_subject(subject)
            if ects_credits < basket["minimum_compulsory_per_subject"]/2:
                return 9999

            plan_total_mandatory_credits += ects_credits

        return basket["minimum_compulsory_total"] - plan_total_mandatory_credits

    def __check_mandatory_credits_one_group(self, plan: Plan,
                                            curriculum: Curriculum,
                                            group_subjects: list) -> int:
        least_exluded = 9999

        for subject in group_subjects:
            subject_return = self.__check_mandatory_credits_one_subject(
                plan, curriculum, subject)

            least_exluded = min(subject_return, least_exluded)

        return least_exluded

    def __check_mandatory_normal_subjects(self, plan: Plan,
                                          curriculum: Curriculum,
                                          excluded_creds: int,
                                          subj_problems: list) -> int:
        simple_subjects = curriculum.return_rules()[
            "national_mandatory_subjects"]

        for subject in simple_subjects:
            subject_return = self.__check_mandatory_credits_one_subject(
                plan, curriculum, subject)
            if subject_return > 0:
                subj_problems["full_credits"] = (subj_problems["full_credits"] +
                            [{"name": "problem_with_simple_subjects", "details": subject}])
            if subject_return > 1000:
                subj_problems["half_credits"] = (subj_problems["half_credits"] +
                            [{"name": "problem_with_simple_subjects", "details": subject}])

            excluded_creds += subject_return

        return excluded_creds

    def __check_mandatory_all_groups(self, plan: Plan,
                                     curriculum: Curriculum,
                                     excluded_credits: int,
                                     group_problems: list) -> int:
        group_subjects = curriculum.return_rules()["group_subjects"]

        for group in group_subjects:
            group_return = self.__check_mandatory_credits_one_group(
                plan, curriculum, group["subjects"])
            if group_return > 0:
                group_problems["full_credits"] = (group_problems["full_credits"] +
                            [{"name": "problem_with_group_subjects", "details": group["name"]}])
            if group_return > 1000:
                group_problems["half_credits"] = (group_problems["half_credits"] +
                            [{"name": "problem_with_group_subjects", "details": group["name"]}])

            excluded_credits += group_return

        return excluded_credits

    def __check_mandatory_all_baskets(self, plan: Plan,
                                      curriculum: Curriculum,
                                      excluded_credits: int,
                                      basket_problems: dict) -> int:
        basket_subjects = curriculum.return_rules()["basket_subjects"]

        for basket in basket_subjects:
            basket_return = self.__check_mandatory_credits_one_basket(
                plan, basket)
            if basket_return > 0:
                basket_problems["full_credits"] = (basket_problems["full_credits"] +
                            [{"name": "problem_with_basket_subjects", "details": basket["name"]}])
            if basket_return > 1000:
                basket_problems["half_credits"] = (basket_problems["half_credits"] +
                            [{"name": "problem_with_basket_subjects", "details": basket["name"]}])

            excluded_credits += basket_return

        return excluded_credits

    def check_total_mandatory(self, plan: Plan,
                              curriculum: Curriculum,
                              mandatory_courses_problems: dict) -> int:
        """Tarkistaa suunnitelman kaikki pakolliset opintopisteet

        Pakolliset opintopisteet voidaan tarkistaa kolmen eri säännön perusteella:
        Normaalit aineet: aineen kaikki pakolliset opintopisteet täytyy löytyä
        Ryhmäaineet: ryhmästä yhden aineen kaikki pakolliset opintopisteet 
                    täytyy löytyä (esim. pitkä tai lyhyt matematiikka)
        Koriaineet: korin jokaisesta aineesta täytyy löytyä jokin vähimmäismäärä opintopisteitä
                    ja korin kokonaisopintopisteille on oma vähimmäismäärä

        Funktio palauttaa puuttuvien opintopisteiden määrän, jotta erityistehtäväpoisluku
        voidaan tarkistaa. Mikäli jossain aineessa puuttuisi kuitenkin yli puolet pakollisista,
        olisi paluuarvo suuruusluokkaa 10000, eli aivan liian suuri.


        Args:
            plan (Plan): Validioitava suunnitelma
            curriculum (Curriculum): Opetussunnitelma, jonka sääntöjä käyetään
            mandatory_courses_problems (dict): Kaksi lista johon validiointivirheet lisätään

        Returns:
            int: Puuttuvien pakollisten opintopisteiden määrä
        """
        excluded_credits = 0

        excluded_credits = self.__check_mandatory_normal_subjects(
            plan, curriculum, excluded_credits, mandatory_courses_problems)
        excluded_credits = self.__check_mandatory_all_groups(
            plan, curriculum, excluded_credits, mandatory_courses_problems)
        excluded_credits = self.__check_mandatory_all_baskets(
            plan, curriculum, excluded_credits, mandatory_courses_problems)

        return excluded_credits
