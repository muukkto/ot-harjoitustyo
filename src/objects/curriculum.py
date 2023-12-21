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

        subject_list = cur_config["subjects"]
        self._subjects = subject_list

    def return_all_subject_codes(self) -> list:
        """Palauttaa kaikki opetussuunnitelmasta löytyvät oppiainekoodit. 
           Samoja ei voi käyttää omissa opintojaksoissa.

        Returns:
            list: Lista oppiainekoodeista.
        """

        all_subject_codes = []

        for subject in self._subjects:
            subject_name = subject["name"]
            all_subject_codes.append(subject_name)

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

    def get_course_from_course_code(self, course_code: str) -> dict:
        """Palauttaa kurssintiedot kurssikoodin perusteella.

        Args:
            course_code (str): Kurssikoodi

        Returns:
            dict: kurssitiedot
        """
        subject_code = self.get_subject_code_from_course_code(course_code)

        for subject in self._subjects:
            if subject_code == subject["name"]:
                for course in subject["courses"]:
                    if course_code == course["name"]:
                        return course

        return None

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

        mandatory_credits = 0

        for subject in self._subjects:
            if subject["name"] == subject_code:
                subject_courses = subject["courses"]

        for course in subject_courses:
            if course["mandatory"]:
                mandatory_credits += course["credits"]

        return mandatory_credits

    def return_all_subjects(self) -> list:
        """Palauttaa kaikki opetussuunnitelman kurssit

        Kurssit on järjestetty listaan oppiaineitain.

        Returns:
            dict: Kaikki kurssi sisältävä lista dict-objekteja
        """
        return self._subjects

    def return_rules(self) -> dict:
        """Palauttaa opetussuunnitelman säännöt

        Returns:
            dict: Säännöt sisältävä dict-objekti
        """
        return self._rules
