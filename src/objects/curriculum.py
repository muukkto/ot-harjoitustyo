from objects.course import Course


class Curriculum:
    """Luokka, joka hallitsee opetussuunnitelmasta riippuvia toiminnallisuuksia.

    Attributes:
        rules: Opetussunnitelman säännöt (tarvitaan suunnitelmian validioinnissa)
        subjects: Opetussuunnitelman kurssit jaettuna oppiaineiden alle.
    """

    def __init__(self, cur_config: dict):
        """Luokan konstruktori, joka luo uuden opetussuunnitelma.

        Args:
            cur_config (dict): Opetussuunnitelman tiedot konfiguraatiotiedostosta.
        """

        self._rules = cur_config["rules"]
        self._subjects = cur_config["subjects"]

    def return_all_subject_codes(self) -> list:
        """Palauttaa kaikki opetussuunnitelmasta löytyvät oppiainekoodit. 
           Samoja ei voi käyttää omissa opintojaksoissa.

        Returns:
            list: Lista oppiainekoodeista.
        """

        all_subject_codes = []

        for subject in self._subjects:
            all_subject_codes.append(subject)

        return all_subject_codes

    def get_subject_code_from_course_code(self, course_code: str) -> str:
        """Palauttaa kurssikoodin alusta oppiainekoodin.

        Args:
            course_code (str):  Kurssinkoodi (esim. ENA1)

        Returns:
            str: Oppiainekoodi (esim. ENA)
        """
        all_subject_codes = self.return_all_subject_codes()

        for subject in all_subject_codes:
            if course_code.startswith(subject):
                return subject

        return None

    def get_course_from_course_code(self, course_code: str) -> Course:
        """Palauttaa Course-objektin kurssikoodin perusteella.

        Args:
            course_code (str): Kurssikoodi

        Returns:
            Course: Course-objekti
        """
        subject_code = self.get_subject_code_from_course_code(course_code)
        return self._subjects[subject_code]["courses"][course_code]

    def get_credits_from_course_code(self, course_code: str) -> int:
        """Palauttaa opintopistemäärän kurssikoodin perusteella.

        Args:
            course_code (str): Kurssikoodi

        Returns:
            int: opintopistemäärä
        """
        course = self.get_course_from_course_code(course_code)
        return course["credits"]

    def get_course_status_from_course_code(self, course_code: str) -> dict:
        """Palauttaa kurssikoodin perustella kurssin validiointitiedot

        Validiointitiedot palautetaan dict-objektina.
        Avain "mandatory" kertoo onko kurssi pakollinen opintojakso
        Avain "national" kertoo onko kurssi valtakunnallinen opintojakso

        Args:
            course_code (str): Kurssikoodi

        Returns:
            dict: Validiointitiedot
        """
        course = self.get_course_from_course_code(course_code)
        return {"mandatory": course["mandatory"], "national": course["national"]}

    def get_mandatory_credits_subject(self, subject_code: str) -> int:
        """Palauttaa oppiaineen pakollisten opintopisteiden määrän.

        Esimerkiksi englannissa on 6 pakollista opintojaksoa,
        joiden yhteenlaksettu opintopistemäärä on 12

        Args:
            subject_code (str): Oppiainekoodi

        Returns:
            int: Pakollisten opintopisteiden määrä.
        """
        subject_courses = self._subjects[subject_code]["courses"]
        mandatory_credits = 0

        for course_code in subject_courses:
            if subject_courses[course_code]["mandatory"]:
                mandatory_credits += subject_courses[course_code]["credits"]

        return mandatory_credits

    # def _return_all_courses(self):
    #    return_list = []
    #    for subject_key in self._subjects.keys():
    #        for course_name in self._subjects[subject_key]["courses"].keys():
    #            ects_credits = self._subjects[subject_key]['courses'][course_name]['credits']
    #            pakollisuus = "pakollinen" if self._subjects[subject_key][
    #                'courses'][course_name]['mandatory'] else "valinnainen"
    #            valtakunnallinen = "Valtakunnallinen" if self._subjects[subject_key][
    #                'courses'][course_name]['national'] else "Paikallinen"
    #            return_list.append(
    #                f"{course_name}  {ects_credits} op  {valtakunnallinen} {pakollisuus}")

    #    return return_list

    def return_all_courses_dict(self) -> dict:
        """Palauttaa kaikki opetussuunnitelman kurssit

        Kurssit on järjestetty dict-objektiin oppiaineitain.

        Returns:
            dict: Kaikki kurssi sisältävä dict-objekti
        """
        return self._subjects

    def return_rules(self) -> dict:
        """Palauttaa opetussuunnitelman säännöt

        Returns:
            dict: Säännöt sisältävä dict-objekti
        """
        return self._rules
