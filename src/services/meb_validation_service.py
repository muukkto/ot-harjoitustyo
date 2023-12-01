import requests


class MebValidationService:
    def validate(self, plan):
        validation_problems = []

        structure_status = self.check_exam_structure(plan)
        timing_status = self.check_exam_timing(plan)

        if structure_status:
            validation_problems.append(
                {"structure_problems": structure_status})

        if timing_status:
            validation_problems.append({"timing_status": timing_status})

        print(validation_problems)
        return validation_problems

    def check_exam_timing(self, plan):
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

        for period in range(1, 4):
            period_exams = set(me_plan[period])

            for day, subjects in same_days.items():
                if len(period_exams.intersection(subjects)) > 1:
                    validation_problems.append(f"too-many-{day}-{period}")

        return validation_problems

    def check_exam_structure(self, plan):
        lang = "fi"

        base_url = f"https://ilmo.ylioppilastutkinto.fi/api/v1/validate?teachingLanguage={lang}"
        exam_parameters = ""

        list_subjects = plan.return_exams_in_meb_plan()

        for subject in list_subjects:
            exam_parameters = exam_parameters + "&exams=" + subject

        request_url = base_url + exam_parameters

        response = requests.get(request_url, timeout=5)

        if response.status_code == 200:
            validation_result = response.json()["validationResult"]
            if validation_result == "ok":
                return []

            return validation_result

        return ["meb-api-not-working"]
