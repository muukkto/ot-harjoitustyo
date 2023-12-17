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

    def test_get_stats(self):
        self.login()
        self.plan_service.add_course("MAA6")
        self.plan_service.add_course("EG3", "Egen kurs", 8, False)
        self.assertEqual(self.plan_service.get_stats()["total_credits"], 11)
