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
        self.assertCountEqual(self.plan_service.get_courses(), ["MAA1"])

    def test_add_course_2(self):
        self.login()
        self.plan_service.add_course("PS2")
        self.plan_service.add_course("ENA5")
        self.assertCountEqual(
            self.plan_service.get_courses(), ["PS2", "ENA5"])

    def test_add_course_3(self):
        self.login()
        self.assertTrue(self.plan_service.add_course("RAA2"))

    def test_cannot_add_course_unlogged(self):
        self.assertFalse(self.plan_service.add_course("MAA1"))

    def test_cannot_add_course_outside_curriculum(self):
        self.login()
        self.plan_service.add_course("AI27")
        self.assertCountEqual(
            self.plan_service.get_courses(), [])

    def test_add_own_course(self):
        self.login()
        self.plan_service.add_course("OMA1", "Oma kurssi", 3, False)
        self.assertCountEqual(self.plan_service.get_courses(), ["OMA1"])

    def test_cannot_add_own_course_two_times(self):
        self.login()
        self.plan_service.add_course("OMA1", "Oma kurssi", 3, False)
        self.plan_service.add_course("OMA1", "Oma kurssi 2", 3, False)
        self.assertCountEqual(self.plan_service.get_courses(), ["OMA1"])

    def test_cannot_add_own_course_with_cur_code(self):
        self.login()
        self.plan_service.add_course(
            "YH2", "Oma kurssi yhteiskuntaopin kurssi", 3, False)
        self.assertCountEqual(self.plan_service.get_courses(), [])

    def test_delete_course_1(self):
        self.login()
        self.plan_service.add_course("HI4")
        self.assertCountEqual(self.plan_service.get_courses(), ["HI4"])
        self.plan_service.delete_course("HI4")
        self.assertCountEqual(self.plan_service.get_courses(), [])

    def test_delete_course_2(self):
        self.login()
        self.plan_service.add_course("S27")
        self.plan_service.add_course("UR1", "Urbaani kurssi", 5, False)
        self.assertCountEqual(
            self.plan_service.get_courses(), ["S27", "UR1"])
        self.plan_service.delete_course("UR1")
        self.assertCountEqual(self.plan_service.get_courses(), ["S27"])

    def test_get_stats(self):
        self.login()
        self.plan_service.add_course("MAA6")
        self.plan_service.add_course("EG3", "Egen kurs", 8, False)
        self.assertIn("Total credits: 11", self.plan_service.get_stats())
