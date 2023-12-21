import unittest

from services.plan_service import PlanService
from services.user_service import UserService
from init_database import initialize_database


class TestPlanService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_service = UserService()
        self.plan_service = PlanService(self.user_service)

    def login(self):
        self.user_service.create_user("User1")
        self.plan_service.create_empty_plan_for_user()

    def test_add_course_1(self):
        self.login()
        self.plan_service.add_course("MAA1")
        self.assertTrue(self.plan_service.get_course_status("MAA1"))

    def test_add_course_2(self):
        self.login()
        self.plan_service.add_course("PS2")
        self.plan_service.add_course("ENA5")
        self.assertTrue(self.plan_service.get_course_status("PS2"))
        self.assertTrue(self.plan_service.get_course_status("ENA5"))

    def test_add_course_3(self):
        self.login()
        self.assertTrue(self.plan_service.add_course("RAA2"))
        self.assertTrue(self.plan_service.get_course_status("RAA2"))

    def test_cannot_add_course_unlogged(self):
        self.assertFalse(self.plan_service.add_course("MAA1"))

    def test_cannot_add_course_outside_curriculum(self):
        self.login()
        self.plan_service.add_course("AI27")
        self.assertFalse(self.plan_service.get_course_status("AI27"))

    def test_add_own_course(self):
        self.login()
        self.plan_service.add_course("OMA1", "Oma kurssi", 3, False)
        self.assertTrue(self.plan_service.get_course_status("OMA1"))

    def test_cannot_add_own_course_two_times(self):
        self.login()
        self.plan_service.add_course("OMA1", "Oma kurssi", 3, False)
        self.plan_service.add_course("OMA1", "Oma kurssi 2", 3, False)
        self.assertEqual(len(self.plan_service.get_own_courses()), 1)

    def test_cannot_add_own_course_with_cur_code(self):
        self.login()
        self.plan_service.add_course(
            "YH2", "Oma kurssi yhteiskuntaopin kurssi", 3, False)
        self.assertFalse(self.plan_service.get_course_status("YH2"))

    def test_delete_course_1(self):
        self.login()
        self.plan_service.add_course("HI4")
        self.assertTrue(self.plan_service.get_course_status("HI4"))
        self.plan_service.delete_course("HI4")
        self.assertFalse(self.plan_service.get_course_status("HI4"))

    def test_delete_course_2(self):
        self.login()
        self.plan_service.add_course("S27")
        self.plan_service.add_course("UR1", "Urbaani kurssi", 5, False)
        self.assertTrue(self.plan_service.get_course_status("UR1"))
        self.plan_service.delete_course("UR1")
        self.assertFalse(self.plan_service.get_course_status("UR1"))
        self.assertTrue(self.plan_service.get_course_status("S27"))

    def test_delete_course_3(self):
        self.login()
        self.assertFalse(self.plan_service.delete_course("MAA7"))

    def test_get_stats(self):
        self.login()
        self.plan_service.add_course("MAA6")
        self.plan_service.add_course("EG3", "Egen kurs", 8, False)
        self.assertEqual(self.plan_service.get_stats()["total_credits"], 11)

    def test_add_legal_meb_exam_1(self):
        self.login()
        self.assertTrue(self.plan_service.add_exam_meb("A", 1))
        self.assertIn("A", self.plan_service.get_meb_plan()[1])

    def test_add_legal_meb_exam_2(self):
        self.login()
        self.assertTrue(self.plan_service.add_exam_meb("FF", 3))
        self.assertIn("FF", self.plan_service.get_meb_plan()[3])

    def test_add_illegal_meb_exam_1(self):
        self.login()
        self.assertFalse(self.plan_service.add_exam_meb("YB", 1))

    def test_add_illegal_meb_exam_2(self):
        self.login()
        self.assertFalse(self.plan_service.add_exam_meb("M", 0))

    def test_delete_meb_exam(self):
        self.login()
        self.plan_service.add_exam_meb("EA", 2)
        self.assertTrue(self.plan_service.remove_exam_meb("EA", 2))
        self.assertCountEqual(self.plan_service.get_meb_plan(), {
                              1: [], 2: [], 3: []})

    def test_illegally_delete_meb_exam_1(self):
        self.login()
        self.plan_service.add_exam_meb("A5", 1)
        self.assertFalse(self.plan_service.remove_exam_meb("A5", 3))
        self.assertIn("A5", self.plan_service.get_meb_plan()[1])

    def test_illegally_delete_meb_exam_2(self):
        self.login()
        self.assertFalse(self.plan_service.remove_exam_meb("HI", 2))

    def test_import_study_plan(self):
        study_plan = {
            "config": {
                "graduation_period": "2024S",
                "meb_language": "sv",
                "special_task": True
            }, "courses": [
                {"on_cur": True, "code": "AI1",
                    "subject": "AI", "name": None, "ects": 0},
                {"on_cur": True, "code": "OP2",
                    "subject": "OP", "name": None, "ects": 0},
                {"on_cur": False, "code": "OMA1", "subject": None,
                    "name": "Oma kurssi 1", "ects": 4}
            ], "meb_plan": {
                1: ["A", "YH"],
                2: ["N", "BB"],
                3: ["BA"]
            }
        }

        self.login()
        self.assertTrue(self.plan_service.import_study_plan(study_plan))

    def test_change_special_task_true(self):
        self.login()
        self.plan_service.change_special_task_status(True)

        self.assertTrue(self.plan_service.get_config()["special_task"])

    def test_change_special_task_false(self):
        self.login()
        self.plan_service.change_special_task_status(False)

        self.assertFalse(self.plan_service.get_config()["special_task"])

    def test_change_meb_language_fi(self):
        self.login()
        self.plan_service.change_meb_language("fi")

        self.assertEqual(self.plan_service.get_config()["meb_language"], "fi")

    def test_change_meb_language_sv(self):
        self.login()
        self.plan_service.change_meb_language("sv")

        self.assertEqual(self.plan_service.get_config()["meb_language"], "sv")

    def test_change_meb_language_wrong_language(self):
        self.login()
        self.plan_service.change_meb_language("jp")

        self.assertEqual(self.plan_service.get_config()["meb_language"], "fi")

    def test_change_graduation_period_autumn(self):
        self.login()
        self.plan_service.change_graduation_period("2025S")

        self.assertEqual(self.plan_service.get_config()
                         ["graduation_period"], "2025S")

    def test_change_graduation_period_spring(self):
        self.login()
        self.plan_service.change_graduation_period("2024K")

        self.assertEqual(self.plan_service.get_config()
                         ["graduation_period"], "2024K")

    def test_change_graduation_period_illegally(self):
        self.login()
        self.plan_service.change_graduation_period("2026U")

        self.assertFalse(self.plan_service.get_config()["graduation_period"])

    def test_courses_save_on_logout(self):
        self.login()
        self.plan_service.add_course("FI2")
        self.plan_service.add_course("ENA5")

        self.user_service.logout()

        new_plan_service = PlanService(self.user_service)

        self.user_service.login("User1")
        new_plan_service.read_plan_for_user()

        self.assertTrue(new_plan_service.get_course_status("FI2"))
        self.assertTrue(new_plan_service.get_course_status("ENA5"))
        self.assertFalse(new_plan_service.get_course_status("MAB6"))
