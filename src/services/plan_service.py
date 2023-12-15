from objects.plan import Plan
from objects.curriculum import Curriculum
from config.config import CURRICULUM

from services.user_service import UserService
from services.validation.validation_service import ValidationService
from services.validation.meb_validation_service import MebValidationService

from repositories import plan_repository


class PlanService:
    """Luokka, joka vastaa opiskelusuunnitelman sovelluslogiikasta.

    Attributes:
        curriculum: Opetussuunnitelma, jonka pohjalta PlanService operoi
        plan: Suunnitelma, jota käsitellään
        user_service: Käyttäjänhallinta ja siihen liittyvät metodit
    """

    def __init__(self, user_service: UserService):
        """Luokan konstruktori. Luo uuden opiskelusuunnitelmasta vastaavan palvelun.

        Args:
            user_service (UserService): Käyttäjänhallinta ja siihen liittyvät metodit
        """
        self._curriculum = Curriculum(CURRICULUM)
        self._plan = None
        self._user_service = user_service

    def create_empty_plan_for_user(self):
        """Luo tyhjän suunnitelman

        Tätä komentoa käytetään heti uuden käyttäjän luomisen jälkeen.
        """
        user = self._user_service.get_current_username()
        if user:
            self._plan = Plan(self._curriculum, user)
            plan_dict = self.get_study_plan()
            plan_repository.save_full_plan(user, plan_dict)

    def read_plan_for_user(self):
        """Lataa tietokannasta vanhan suunnitelman

        Tätä komentoa käytetään heti sisäänkirjautumisen jälkeen.
        """
        user = self._user_service.get_current_username()
        if user:
            old_study = plan_repository.return_plan(user)
            self.import_study_plan(old_study)

    def add_course(self, course_code: str, name: str = None,
                   ects_credits: str = 0, in_cur: bool = True) -> bool:
        """Lisää kurssi suunnitelmaan

        Args:
            course_code (str): Kurssikoodi
            name (str, optional): Kurssin nimi. Oletuksena None.
            ects_credits (str, optional): Kurssin opintopistemäärä. Oletuksena 0.
            in_cur (bool, optional): Löytyykö kurssi opetussuunnitelmasta. Oletuksena True.

        Returns:
            bool: Onnistuiko kurssin tallennus
        """
        current_user = self._user_service.get_current_username()
        if current_user:
            if in_cur:
                course = self._plan.add_curriculum_course_to_plan(course_code)
            else:
                course = self._plan.add_own_course_to_plan(
                    course_code, name, ects_credits)

            if course:
                plan_repository.add_course(current_user, course)
                return True

        return False

    def delete_course(self, course_code: str) -> bool:
        """Poista kurssi suunnitelmasta

        Args:
            course_code (str): Kurssikoodi

        Returns:
            bool: Onnistuiko poistaminen
        """
        current_user = self._user_service.get_current_username()
        if current_user:
            if self._plan.delete_course_from_plan(course_code):
                plan_repository.delete_course(current_user, course_code)

        return False

    def get_curriculum_tree(self) -> dict:
        """Palauttaa suunnitelmaan liittyvän opetussuunnitelman

        Opetussuunnitelma on järjestetty oppiaineiden mukaisesti.

        Returns:
            dict: Opetussuunnitelman kurssit dict-objektina
        """
        return self._plan.get_curriculum_tree()

    def get_course_status(self, course_code: str) -> bool:
        """Palauttaa tiedon onko kurssi suunnitelmassa

        Args:
            course_code (str): Kurssikoodi

        Returns:
            bool: True = kurssi on suunnitelmassa, False = kurssi ei ole suunnitelmassa
        """
        return self._plan.check_if_course_on_plan(course_code)

    def get_stats(self) -> dict:
        """Palauttaa tilastoja suunnitelmasta 

        Saatavilla on tilastot:
        total_credits
        mandatory_credits
        national_voluntary_credits
        local_voluntary_credits

        Returns:
            dict: Tilastot
        """
        total_credits = self._plan.get_total_credits_on_plan()
        mandatory_credits = self._plan.get_credits_by_criteria(mandatory=True,
                                                               national=True)

        national_voluntary_credits = self._plan.get_credits_by_criteria(mandatory=False,
                                                                        national=True)

        local_voluntary_credits = self._plan.get_credits_by_criteria(mandatory=False,
                                                                     national=False)

        local_voluntary_credits += self._plan.get_credits_own_course()

        return_stats = {}
        return_stats["total_credits"] = total_credits
        return_stats["mandatory_credits"] = mandatory_credits
        return_stats["national_voluntary_credits"] = national_voluntary_credits
        return_stats["local_voluntary_credits"] = local_voluntary_credits

        return return_stats

    def check_reserved_codes(self, course_code: str) -> bool:
        """Tarkistaa onko kurssikoodi varattu opetussuunnitelman kurssille

        Args:
            course_code (str): Kurssikoodi

        Returns:
            bool: True = kurssikoodi on varattu, False = kurssikoodi on vapaa
        """
        if self._curriculum.get_subject_code_from_course_code(course_code):
            return True

        return False

    def validate_plan(self) -> list:
        """Validioi suunnitelman

        Returns:
            list: Validiointivirheet (jos tyhjä validiointi meni läpi)
        """
        validation_service = ValidationService()
        validation_status = validation_service.validate(
            self._plan, self._curriculum)

        return validation_status

    def get_course_codes(self) -> list:
        """Palauttaa listan kaikista suunnitelmalta löytyvistä kursseista

        Returns:
            list: Lista kurssikoodeista
        """
        return_codes = []
        courses = self._plan.get_courses_on_plan()
        for course in courses:
            return_codes.append(course.get_code())

        return return_codes

    def get_own_courses(self) -> list:
        """Palauttaa listan suunnitelman omista kursseista

        Returns:
            list: Lista omista kursseista.
        """
        return self._plan.get_own_courses_on_plan()

    def add_exam_meb(self, exam_code: str, exam_period: int) -> bool:
        """Lisää koe YO-suunnitelmaan

        Args:
            exam_code (str): Koekoodi
            exam_period (int): Kokeen suoritusajankohta

        Returns:
            bool: Onnistuiko lisäys
        """
        current_user = self._user_service.get_current_username()
        if current_user:
            if self._plan.add_exam_to_meb_plan(exam_code, exam_period):
                plan_repository.add_meb_exam(
                    current_user, exam_code, exam_period)
                return True
        return False

    def remove_exam_meb(self, exam_code: str, exam_period: int) -> bool:
        """Poista koe YO-suunnitelmasta

        Args:
            exam_code (str): Koekoodi
            exam_period (int): Kokeen suoritusajankohta

        Returns:
            bool: Onnistuiko poisto
        """
        current_user = self._user_service.get_current_username()
        if current_user:
            if self._plan.remove_exam_from_meb_plan(exam_code, exam_period):
                plan_repository.delete_meb_exam(
                    current_user, exam_code, exam_period)
                return True

        return False

    def validate_meb(self) -> dict:
        """Validioi YO-suunnitelma

        Returns:
            dict: Validioinnin virheet (tyhjä jos validiointi menee läpi)
        """
        validation_service = MebValidationService()
        return validation_service.validate(self._plan)

    def get_study_plan(self) -> dict:
        """Palauttaa koko opintosuunnitelman

        Suunnitelma muodostuu kolmesta osasta:
        - Tieto eritystehtävästä
        - Suunnitelmaan kuuluvat kurssit
        - YO-suunnitelma

        Returns:
            dict: Opiskelusuunnitelma dict-objektina
        """
        return self._plan.return_study_plan()

    def import_study_plan(self, study_plan: dict) -> bool:
        """Tuo opiskelusuunnitelma

        Args:
            study_plan (dict): Opiskelusuunnitelma

        Returns:
            bool: Onnistuiko tuonti
        """
        current_user = self._user_service.get_current_username()
        if current_user:
            new_plan = Plan(self._curriculum, current_user)
            self._plan = new_plan

            if self._plan.import_study_plan(study_plan):
                plan_repository.save_full_plan(current_user, study_plan)
                return True

        return False

    def get_meb_plan(self) -> dict:
        """Palauta YO-suunnitelma

        Returns:
            dict: YO-suunnitelma dict-objektina
        """
        return self._plan.return_meb_plan()

    def change_special_task_status(self, new_status: bool):
        """Muuta suunnitelman erityistehtävästatus

        True = suunnitelma noudattaa erityistehtävätuntijakoa
        False = suunnitelma noudattaa normaalia tuntijakoa

        Args:
            new_status (bool): Uusi erityistehtävästatus
        """
        current_user = self._user_service.get_current_username()
        if current_user:
            self._plan.change_special_task(new_status)
            plan_repository.change_config(current_user, self._plan.return_config())

    def change_meb_language(self, new_meb_language: str):
        """Muuta YO-suunnitelman kieli

        Vaihtoedhto sv ja fi

        Args:
            new_meb_language (str): Uusi kieli
        """        
        current_user = self._user_service.get_current_username()
        if current_user:
            self._plan.change_meb_language(new_meb_language)
            plan_repository.change_config(current_user, self._plan.return_config())

    def change_graduation_period(self, new_period: str):
        """Muuta valmistumisajnakohdan

        Vaihtoehdot muotoa 2023S tai 2023K

        Args:
            new_period (str): Uusi ajankohta
        """        
        current_user = self._user_service.get_current_username()
        if current_user:
            self._plan.change_graduation_period(new_period)
            plan_repository.change_config(current_user, self._plan.return_config())

    def get_config(self) -> dict:
        """Palauttaa suunnitelman konfigurointitiedot

        Saatavilla on tiedot:
        special_task
        meb_language
        graduation_period

        Returns:
            dict: Konfigurointiedot
        """
        return self._plan.return_config()
