import requests

from config.config import MAX_MEB_PERIODS
from objects.plan import Plan


class MebValidationService:
    """Luokka, joka vastaa YO-suunnitelman validioinnista
    """

    def validate(self, plan: Plan) -> dict:
        """Validioi YO-suunnitelman

        Paluuarvona on sanakirja virheistä. Mikäli dict on tyhjä, ei virheitä löydy.
        Indeksillä "structure_problems" on YO-suunnitelman rakenteeseen
        liittyvät virheet. Esim. liian vähän aineita. 
        Indeksillä "timing_problems" on virheet, jotka johtuvat, että suunnitelmasta
        löytyy kaksi ainetta samalla päivälle.

        Args:
            plan (Plan): Opintosuunnitelma

        Returns:
            dict: Validioinnin virheet
        """
        validation_problems = {}

        structure_status = self._check_exam_structure(plan)
        timing_status = self._check_exam_timing(plan)

        if structure_status:
            validation_problems["structure_problems"] = structure_status

        if timing_status:
            validation_problems["timing_problems"] = timing_status

        return validation_problems

    def _check_exam_timing(self, plan: Plan) -> list:
        same_days = {
            "mother_tongue": ("A", "A5", "O", "O5"),
            "nat_and_hum_day_1": ("UO", "UE", "ET", "YH", "KE", "GE", "TE"),
            "nat_and_hum_day_2": ("PS", "FF", "HI", "FY", "BI"),
            "long_foreign": ("EA", "FA", "PA", "SA", "VA"),
            "short_foreign": ("EC", "FC", "PC", "SC", "VC", "TC",
                              "GC", "L1", "L7", "IC", "DC", "QC"),
            "second_national": ("BA", "BB", "CA", "CB"),
            "maths": ("N", "M"),
            "sami": ("I", "W", "Z")
        }

        validation_problems = []

        me_plan = plan.return_meb_plan()

        for period in range(1, MAX_MEB_PERIODS+1):
            period_exams = set(me_plan[period])

            for day, subjects in same_days.items():
                if len(period_exams.intersection(subjects)) > 1:
                    validation_problems.append(f"too-many-{day}-{period}")

        return validation_problems

    def _check_exam_structure(self, plan: Plan) -> list:
        lang = "fi"

        base_url = (f"https://ilmo.ylioppilastutkinto.fi/api/v1/"
                    f"validate?teachingLanguage={lang}")
        exam_parameters = ""

        list_subjects = plan.return_exams_in_meb_plan()

        for subject in list_subjects:
            exam_parameters = exam_parameters + "&exams=" + subject

        request_url = base_url + exam_parameters

        response = requests.get(request_url, timeout=5)

        if response.status_code == 200:
            validation_result = response.json()["validationResult"]
            if validation_result == "ok":
                return None

            return validation_result

        return "meb-api-not-working"
