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
            if(course_code.find(subject)!=-1):
                return subject
            
        return None

    def get_credits_from_course_code(self, course_code):
        return self.subjects[self.get_subject_code_from_course_code(course_code)]["courses"][course_code]["credits"]
    

    def print_courses(self):
        for subject_key in self.subjects.keys():
            for course_name in self.subjects[subject_key]["courses"].keys():
                credits = self.subjects[subject_key]['courses'][course_name]['credits']
                pakollisuus = "pakollinen" if self.subjects[subject_key]['courses'][course_name]['mandatory'] else "valinnainen"
                valtakunnallinen = "Valtakunnallinen" if self.subjects[subject_key]['courses'][course_name]['national'] else "Paikallinen"
                print(f"{course_name}  {credits} op  {valtakunnallinen} {pakollisuus}")

    def print_rules(self):
        print(f"minimum credits: {self.rules['minimum_credits']}")
        print(f"minimum national voluntary credits: {self.rules['minimum_national_voluntary_credits']}")
        print(f"code for special task courses: {self.rules['special_task_code']}")
        print(f"subjects classified as mother tongue: {self.rules['mother_tongue']}")
        print(f"subjects classified as second national language: {self.rules['second_national_language']}")
        print(f"subjects classified as long foreign language: {self.rules['long_foreign_language']}")
        print(f"subjects classified as maths: {self.rules['maths']}")
        print(f"subjects classified as national mandatory subjects: {self.rules['national_mandatory_subjects']}")
        print(f"subjects classified as national voluntary subjects: {self.rules['national_voluntary_subjects']}")
        print(f"rules for art basket: {self.rules['basket_subjects']['arts']}")