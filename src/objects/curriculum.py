class Curriculum:
    def __init__(self, cur_config):
        self.rules = cur_config["rules"]
        self.subjects = cur_config["subjects"]

    def return_all_subject_codes(self):
        all_subject_codes = []

        for subject in self.subjects:
            all_subject_codes.append(subject)

        return all_subject_codes

    def get_subject_code_from_course_code(self, course_code):
        all_subject_codes = self.return_all_subject_codes()

        for subject in all_subject_codes:
            if course_code.startswith(subject):
                return subject

        return None

    def get_course_from_course_code(self, course_code):
        subject_code = self.get_subject_code_from_course_code(course_code)
        return self.subjects[subject_code]["courses"][course_code]

    def get_credits_from_course_code(self, course_code):
        course = self.get_course_from_course_code(course_code)
        return course["credits"]

    def get_course_status_from_course_code(self, course_code):
        course = self.get_course_from_course_code(course_code)
        return {"mandatory": course["mandatory"], "national": course["national"]}

    def get_mandatory_credits_subject(self, subject_code):
        subject_courses = self.subjects[subject_code]["courses"]
        mandatory_credits = 0

        for course_code in subject_courses:
            if subject_courses[course_code]["mandatory"]:
                mandatory_credits += subject_courses[course_code]["credits"]

        return mandatory_credits

    def return_all_courses(self):
        return_list = []
        for subject_key in self.subjects.keys():
            for course_name in self.subjects[subject_key]["courses"].keys():
                ects_credits = self.subjects[subject_key]['courses'][course_name]['credits']
                pakollisuus = "pakollinen" if self.subjects[subject_key][
                    'courses'][course_name]['mandatory'] else "valinnainen"
                valtakunnallinen = "Valtakunnallinen" if self.subjects[subject_key][
                    'courses'][course_name]['national'] else "Paikallinen"
                return_list.append(
                    f"{course_name}  {ects_credits} op  {valtakunnallinen} {pakollisuus}")

        return return_list

    def print_rules(self):  # pragma: no cover
        # tämä pois pylint ja coverage, koska pelkästään kehityksen aikaiseen testailuun
        # pylint: disable=line-too-long
        print(f"minimum credits: {self.rules['minimum_credits']}")
        print(
            f"minimum national voluntary credits: {self.rules['minimum_national_voluntary_credits']}")
        print(
            f"code for special task courses: {self.rules['special_task_code']}")
        print(
            f"subjects classified as mother tongue: {self.rules['mother_tongue']}")
        print(
            f"subjects classified as 2nd national lang: {self.rules['second_national_language']}")
        print(
            f"subjects classified as long foreign lang: {self.rules['long_foreign_language']}")
        print(f"subjects classified as maths: {self.rules['maths']}")
        print(
            f"subjects classified as nat mandatory subjects: {self.rules['national_mandatory_subjects']}")
        print(
            f"subjects classified as nat voluntary subjects: {self.rules['national_voluntary_subjects']}")
        print(f"rules for art basket: {self.rules['basket_subjects']['arts']}")
