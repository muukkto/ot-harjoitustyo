class Course:
    """Luokka, joka vastaa kurssien suoritustiedoista

    Attributes:
        code: Kurssin koodi
        on_plan: Löytyykö kurssi suunnitelmasta
        on_cur: Löytyykö kurssi opetussuunnitelmasta
        subject: Kurssin oppiaine (käytössä vain omilla kursseilla)
        name: Kurssin nimi (käytössä vain omilla kursseilla)
        ects: Kurssin opintopisteiden määrä (käytössä vain omilla kursseilla)
    """

    def __init__(self, code: str,
                 subject: str = None,
                 on_cur: bool = True,
                 name: str = None,
                 ects: int = 0):
        """Luokan konstruktori, joka luo uuden kurssin.

        Args:
            code (str): Kurssin koodi
            subject (str, optional): Kurssin oppiaine (käytössä vain omilla kursseilla)
            on_cur (bool, optional): Löytyykö kurssi opetussuunnitelmasta. Oletuksena True
            name (str, optional): Kurssin nimi (käytössä vain omilla kursseilla)
            ects (int, optional): Kurssin opintopisteiden määrä (käytössä vain omilla kursseilla)
        """

        self._code = code
        self._on_cur = on_cur
        self._subject = subject
        self._name = name
        self._ects = ects
        if self._on_cur:
            self._on_plan = False
        else:
            self._on_plan = True

    def change_status(self, new_status: bool):
        """Vaihtaa kurssin statuksen. True = mukana opintosuunnitelmassa.

        Args:
            new_status (bool): Kurssin uusi status
        """

        self._on_plan = new_status

    def get_status(self) -> bool:
        """Palauttaa kurssin nykyisen statuksen.

        Returns:
            bool: Kurssin nykyinen status.
        """

        return self._on_plan

    def get_ects(self) -> int:
        """Palauttaa kurssin opintopistemäärän. 

        Jos kurssi löytyy opetussuunnitelmasta, 
        ei palauteta mitään.

        Returns:
            int: Opintopistemäärä.
        """
        if not self._on_cur:
            return self._ects

        return None

    def get_code(self) -> str:
        """Palauttaa kurssikoodin

        Returns:
            str: Kurssikoodi
        """

        return self._code

    def __str__(self) -> str:
        """Määritetään kurssin merkkijonomuoto

        Returns:
            str: Kurssin merkkijonomuoto (eli kurssikoodi)
        """

        return self._code

    def to_json(self) -> dict:
        """Palauttaa kurssin tiedot, jotta kurssit saadaan tallennettua JSON-tiedostoon.

        Returns:
            dict: Kurssin tiedot dict-objektina
        """
        json_object = {"on_cur": self._on_cur,
                       "code": self._code,
                       "subject": self._subject,
                       "name": self._name,
                       "ects": self._ects}

        return json_object
