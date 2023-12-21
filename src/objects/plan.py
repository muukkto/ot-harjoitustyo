import re

from objects.course import Course
from objects.curriculum import Curriculum

from config.meb_config import get_meb_codes

from config.config import MAX_MEB_PERIODS


class Plan:
    """Luokka, joka vastaa opiskelusuunnitelmasta 

    Luokka säilöö tiedon sekä opetussuunnitelmaan kuuluvista kursseista, että omista kursseista.
    Luokka säilöö myös ylioppilastutkintosuunnitelman.


    Attributes:
        curriculum: Opetussuunnitelma, jonka perusteella opiskelusuunnitelma on luotu
        cur_courses: Opetussuunnitelmasta löytyvien kurssien tiedot.
        own_courses: Omien kurssien tiedot.
        special_task: Noudattaako suunnitelma erityistehtävätuntijakoa.
        username: Suunnitelman käyttäjätunnus
        meb_plan: Ylioppilastutkintosuunnitelma
        meb_language: Millä kielellä YO-tutkintosuoritetaan (tällä hetkellä tuki vain fi)


    """

    def __init__(self, curriculum: Curriculum, username: str):
        """Luokan konstruktori, joka luo tyhjän opiskelusuunnitelman.

        Tyhjässä suunnitelmassa on kaikki opetusuunnitelmasta löytyvät kurssit statuksella False. 
        Erityistehtävästatus on oletuksena False.
        Omille kursseille ja ylioppilastutkintosuunnitelmalle löytyy tyhjät rakenteet.

        Args:
            curriculum (Curriculum): Opetusuunnitelma, jonka perusteella suunnitelma luodaan.
            username (str): Opetussuunnitelman käyttäjätunnus
        """
        self._curriculum = curriculum
        self._cur_courses = {}
        self._own_courses = {}
        self._special_task = False

        self._username = username

        self._meb_language = "fi"
        self._graduation_period = None

        self._meb_plan = {}
        for i in range(1, MAX_MEB_PERIODS+1):
            self._meb_plan[i] = []

        for subject in curriculum.return_all_subjects():
            subject_code = subject["name"]
            subject_courses = subject["courses"]

            self._cur_courses[subject_code] = {}

            for course in subject_courses:
                course_name = course["name"]
                self._cur_courses[subject_code][course_name] = Course(
                    course_name, subject_code, True)

    def get_curriculum_tree(self) -> dict:
        """Palauttaa suunnitelmaan liittyvän opetusuunnitelman.

        Returns:
            dict: Kaikki opetussuunnitelman kurssit sisältävä dict-objekti.
        """
        return self._curriculum.return_all_subjects()

    def add_course_to_plan(self, code: str,
                                 name: str = None,
                                 ects_credits: int = 0,
                                 on_cur: bool = True) -> Course:
        """Lisää kurssin suunnitelmaan

        Args:
            code (str): Kurssikoodi
            name (str, optional): Kurssin nimi. Oletuksena None.
            ects_credits (int, optional): Opintopistemäärä. Oletuksena 0.
            on_cur (bool, optional): Kuuluuko kurssi opetussuunnitelmaan. Oletuksena True.

        Returns:
            Course: Lisätty kurssiobjekti. Palauttaa None mikäli kurssin lisääminen ei onnistu.
        """

        if on_cur:
            return self._add_curriculum_course_to_plan(code)

        return self._add_own_course_to_plan(code, name, ects_credits)

    def _add_curriculum_course_to_plan(self, code: str) -> Course:
        """Lisää opetussuunnitelmasta löytyvän kurssin suunnitelmaan.

        Args:
            code (str): Kurssikoodi

        Returns:
            Course: Lisätty kurssiobjekti. Palauttaa None mikäli kurssia ei löydy.
        """
        course = self.__find_cur_course(code)
        if course:
            course.change_status(True)
            return course

        return None

    def _add_own_course_to_plan(self, code: str, name: str, ects_credits: int) -> Course:
        """Lisää oman kurssin suunnitelmaan.

        Args:
            code (str): Kurssikoodi
            name (str): Kurssin nimi
            ects_credits (int): Opintopistemäärä

        Returns:
            Course: Lisätty kurssiobjekti. Palauttaa None mikäli kurssia ei voida lisätä.
        """
        course = self.__find_own_course(code)
        subject = self._curriculum.get_subject_code_from_course_code(code)
        if not course and not subject:
            new_course = Course(code, on_cur=False,
                                name=name, ects=ects_credits)
            self._own_courses[code] = new_course
            return new_course

        return None

    def delete_course_from_plan(self, code: str) -> bool:
        """Poistaa kurssin suunnitelmasta

        Args:
            code (str): Kurssikoodi

        Returns:
            bool: True mikäli poistaminen onnistui ja False mikäli poistaminen epäonnistui.
        """
        course = self.__find_cur_course(code)
        if course:
            course.change_status(False)
            return True

        own_course = self.__find_own_course(code)
        if own_course:
            del self._own_courses[code]
            return True

        return False

    def __find_cur_course(self, course_code: str) -> Course:
        subject_code = self._curriculum.get_subject_code_from_course_code(
            course_code)

        if subject_code:
            if course_code in self._cur_courses[subject_code]:
                return self._cur_courses[subject_code][course_code]

        return None

    def __find_own_course(self, course_code: str) -> Course:
        if course_code in self._own_courses:
            return self._own_courses[course_code]

        return None

    def check_if_course_on_plan(self, course_code: str) -> bool:
        """Palauttaa tiedon onko kurssi suunnitelmassa.

        Args:
            course_code (str): Kurssikoodi

        Returns:
            bool: True jos kurssi löytyy suunnitelmasta, False muulloin.
        """
        found_course = self.__find_cur_course(course_code)
        if found_course:
            return found_course.get_status()

        found_course_2 = self.__find_own_course(course_code)
        if found_course_2:
            return found_course_2.get_status()

        return False

    def get_courses_on_plan(self) -> list:
        """Palauttaa listan suunnitelman kursseista

        Returns:
            list: Suunnitelmasta löytyvät kurssit
        """
        cur_courses = self.__get_curriculum_courses_on_plan()
        own_courses = self.get_own_courses_on_plan()

        return cur_courses + own_courses

    def __get_curriculum_courses_on_plan(self, subject_code: str = None) -> list:
        planned_courses = []

        if subject_code:
            for course in self._cur_courses[subject_code].values():
                if course.get_status():
                    planned_courses.append(course)
        else:
            for subject in self._cur_courses.values():
                for course in subject.values():
                    if course.get_status():
                        planned_courses.append(course)

        return planned_courses

    def get_own_courses_on_plan(self) -> list:
        """Palauttaa listan suunnitelman omista kursseista

        Returns:
            list: Suunnitelmalta löytyvät omat kurssit
        """
        planned_courses = []
        for course in self._own_courses.values():
            planned_courses.append(course)

        return planned_courses

    def get_credits_by_criteria(self, mandatory: bool, national: bool, subject: str = None) -> int:
        """Palauttaa hakuehtojen mukaisen opintopistemäärä

        Args:
            mandatory (bool): True = pakollisey opintojaksot, False = valinnaiset opintojaksot
            national (bool): True = valtakunnalliset opintojaksot, False = paikalliset opintojaksot
            subject (str, optional): Oppiainekoodi. Oletuksena None.

        Returns:
            int: Opintopistemäärä
        """
        total_credits = 0
        for course in self.__get_curriculum_courses_on_plan(subject):
            course_code = course.get_code()
            course_status = self._curriculum.get_course_status_from_course_code(
                course_code)
            if course_status["mandatory"] == mandatory and course_status["national"] == national:
                course_credits = self._curriculum.get_credits_from_course_code(
                    course_code)
                total_credits += course_credits

        return total_credits

    def get_credits_own_course(self) -> int:
        """Palauttaa omien kurssien opintopistemäärän.

        Returns:
            int: Opintopistemäärä
        """
        total_credits = 0

        for course in self.get_own_courses_on_plan():
            total_credits += course.get_ects()

        return total_credits

    def get_mandatory_credits_subject(self, subject_code: str) -> int:
        """Palauttaa yksittäisen oppaineen pakollisten opintopisteiden määrän.

        Args:
            subject_code (str): Oppiainekoodi

        Returns:
            int: Opintopistemäärä
        """
        return self.get_credits_by_criteria(mandatory=True, national=True, subject=subject_code)

    def get_total_credits_on_plan(self) -> int:
        """Palauttaa suunnitelman opintopisteiden kokonaismäärän

        Returns:
            int: Opintopistemäärä
        """
        total_credits = 0
        total_credits += self.get_credits_by_criteria(True, True)
        total_credits += self.get_credits_by_criteria(False, True)
        total_credits += self.get_credits_by_criteria(False, False)
        total_credits += self.get_credits_by_criteria(True, False)
        total_credits += self.get_credits_own_course()

        return total_credits

    def add_exam_to_meb_plan(self, exam_code: str, examination_period: int) -> bool:
        """Lisää kokeen ylioppilastutkintosuunnitelmaan

        Args:
            exam_code (str): Koekoodi (vaihtoehdot config-kansiossa "meb_course_codes.csv")
            examination_period (int): Kokeen suoritusajankohta (0 ja MAX_MEB_PERIODS välistä)

        Returns:
            bool: Onnistuiko tallentaminen
        """
        if (exam_code in get_meb_codes(self._meb_language)
                and MAX_MEB_PERIODS >= examination_period > 0):
            self._meb_plan[examination_period].append(
                exam_code)
            return True

        return False

    def remove_exam_from_meb_plan(self, exam_code: str, examination_period: int) -> bool:
        """Poistaa kokeen ylioppilastutkintosuunnitelmasta

        Args:
            exam_code (str): Koekoodi (täytyy löytyä config-kansion
                             "meb_course_codes.csv" tiedostosta)
            examination_period (int): Kokeen suoritusajankohta (täytyy olla 0 ja
                                      MAX_MEB_PERIODS välistä)

        Returns:
            bool: Onnistuiko poistaminen
        """
        if (exam_code in get_meb_codes(self._meb_language)
                and MAX_MEB_PERIODS >= examination_period > 0):
            sub_list = self._meb_plan[examination_period]
            if exam_code in sub_list:
                sub_list.remove(exam_code)
                self._meb_plan[examination_period] = sub_list

                return True

        return False

    def return_meb_plan(self) -> dict:
        """Palauttaa ylioppilastutkintosuunnitelman

        Returns:
            dict: YO-suunnitelma dict-objektina
        """
        return self._meb_plan

    def change_special_task(self, status: bool):
        """Muuttaa suunnitelman erityistehtävästatuksen

        Args:
            status (bool): Uusi status
        """
        self._special_task = status

    def change_meb_language(self, language: str) -> bool:
        """Muuttaa yo-tutkinnon kielen. 

        Sallitut vaihtoehdot ovat "fi" ja "sv".

        Args:
            language (str): Uusi kieli

        Returns:
            bool: Onnistuiko vaihtaminen
        """

        if language in ("fi", "sv"):
            self._meb_language = language
            return True

        return False

    def change_graduation_period(self, new_period) -> bool:
        """Vaihtaa valmistumisajankohdan.

        Uuden ajankohdan täytyy olla muotoa 2023S tai 2024K

        Args:
            new_period (_type_): Uusi ajankohta

        Returns:
            bool: Onnistuiko muutos
        """

        if re.fullmatch(r"20\d{2}[KS]", new_period):
            self._graduation_period = new_period
            return True

        return False

    def return_config(self) -> dict:
        """Palauttaa suunnitelman konffaustiedot

        Vastauksessa on avaimet:
        "special_task"
        "meb_language"
        "graduation_period"

        Returns:
            dict: configtiedot sanakirjana
        """

        return ({"special_task": self._special_task,
                 "meb_language": self._meb_language,
                 "graduation_period": self._graduation_period})

    def return_study_plan(self) -> dict:
        """Palauttaa koko opiskelusuunnitelman

        Suunnitelma muodostuu kolmesta osasta:
        - Konffaustiedot
        - Suunnitelmaan kuuluvat kurssit
        - YO-suunnitelma

        Returns:
            dict: Opiskelusuunnitelma dict-objektina
        """
        plan_json_object = {}
        plan_json_object["config"] = self.return_config()

        courses = []

        for course in self.get_courses_on_plan():
            if course.get_status():
                courses.append(course.to_json())

        plan_json_object["courses"] = courses

        meb_plan = self.return_meb_plan()

        plan_json_object["meb_plan"] = meb_plan

        return plan_json_object

    def return_exams_in_meb_plan(self) -> list:
        """Palauttaa listan uniikeista YO-aineista

        Returns:
            list: Uniikit YO-aineet
        """
        all_exams = set()

        for i in range(1, MAX_MEB_PERIODS+1):
            all_exams.update(self._meb_plan[i])

        return list(all_exams)

    def import_study_plan(self, study_plan: dict) -> bool:
        """Tuo opiskelusuunnitelman dict-objektista

        Args:
            study_plan (dict): Opiskelusuunnitelma

        Returns:
            bool: Onnistuiko tuonti
        """
        self._special_task = study_plan["config"]["special_task"]
        self._meb_language = study_plan["config"]["meb_language"]
        self._graduation_period = study_plan["config"]["graduation_period"]

        courses = study_plan["courses"]
        for course in courses:
            if course["on_cur"]:
                self.add_course_to_plan(course["code"], on_cur=True)
            else:
                self.add_course_to_plan(
                    course["code"], course["name"], course["ects"], on_cur=False)

        meb_plan = study_plan["meb_plan"]
        for (period, exams) in meb_plan.items():
            for exam in exams:
                self.add_exam_to_meb_plan(exam, period)

        return True
