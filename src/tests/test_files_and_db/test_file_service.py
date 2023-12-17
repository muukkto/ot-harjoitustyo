import unittest

from objects.plan import Plan
from objects.curriculum import Curriculum

from config.config import CURRICULUM


class TestFileImport(unittest.TestCase):
    def setUp(self):
        curriculum = Curriculum(CURRICULUM)
        self.plan = Plan(curriculum, "User1")

    def test_plan_can_import_dict(self):
        study_plan = {
            "config": {
                "graduation_period": "2023K",
                "meb_language": "fi",
                "special_task": False
            }, "courses": [
                {"on_cur": True, "code": "AI1", "subject": "AI", "name": None, "ects": 0},
                {"on_cur": True, "code": "OP2", "subject": "OP", "name": None, "ects": 0},
                {"on_cur": False, "code": "OMA1", "subject": None, "name": "Oma kurssi 1","ects": 4}
            ], "meb_plan": {
                1: ["A"],
                2: ["M", "FF"],
                3: []
            }
        }

        self.assertTrue(self.plan.import_study_plan(study_plan))

        self.assertTrue(self.plan.check_if_course_on_plan("AI1"))
        self.assertTrue(self.plan.check_if_course_on_plan("OMA1"))
        self.assertFalse(self.plan.check_if_course_on_plan("ENA6"))

        self.assertCountEqual(self.plan.return_meb_plan()[1], ["A"])
        self.assertCountEqual(self.plan.return_meb_plan()[2], ["M", "FF"])

    def test_return_study_plan_correct_format(self):
        self.plan.add_curriculum_course_to_plan("SAA3")
        self.plan.add_curriculum_course_to_plan("OP1")
        self.plan.add_curriculum_course_to_plan("FY5")

        self.plan.add_own_course_to_plan("EGE1", "EGEN KURS 1", 5)

        correct_study_plan = {
            'config': {'special_task': False, 
                       'meb_language': 'fi', 
                       'graduation_period': None}, 
            'courses': [{'on_cur': True, 
                         'code': 'SAA3', 
                         'subject': 'SAA', 
                         'name': None, 
                         'ects': 0}, 
                         {'on_cur': True, 
                          'code': 'FY5',
                          'subject': 'FY',
                          'name': None,
                          'ects': 0}, 
                         {'on_cur': True, 
                          'code': 'OP1',
                          'subject': 'OP',
                          'name': None,
                          'ects': 0}, 
                         {'on_cur': False,
                          'code': 'EGE1',
                          'subject': None,
                          'name': 'EGEN KURS 1',
                          'ects': 5}], 
            'meb_plan': {1: [], 2: [], 3: []}}

        self.assertDictEqual(self.plan.return_study_plan(), correct_study_plan)


class TestFileService(unittest.TestCase):
    def setUp(self):
        pass
