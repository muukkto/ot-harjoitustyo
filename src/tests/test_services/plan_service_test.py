import unittest

from services.plan_service import PlanService


class TestPlanService(unittest.TestCase):
    def setUp(self):
        self.plan_service = PlanService()

    def test_add_course_1(self):
        self.plan_service.add_course("MAA1")
        self.assertCountEqual(self.plan_service.print_courses(), ["MAA1"])

    def test_add_course_2(self):
        self.plan_service.add_course("PS02")
        self.plan_service.add_course("ENA5")
        self.assertCountEqual(
            self.plan_service.print_courses(), ["PS02", "ENA5"])

    def test_add_own_course(self):
        self.plan_service.add_course("OMA1", "Oma kurssi", 3, False)
        self.assertCountEqual(self.plan_service.print_courses(), ["OMA1"])

    def test_delete_course_1(self):
        self.plan_service.add_course("HI4")
        self.assertCountEqual(self.plan_service.print_courses(), ["HI4"])
        self.plan_service.delete_course("HI4")
        self.assertCountEqual(self.plan_service.print_courses(), [])

    def test_delete_course_2(self):
        self.plan_service.add_course("S27")
        self.plan_service.add_course("UR1", "Urbaani kurssi", 5, False)
        self.assertCountEqual(
            self.plan_service.print_courses(), ["S27", "UR1"])
        self.plan_service.delete_course("UR1")
        self.assertCountEqual(self.plan_service.print_courses(), ["S27"])

    def test_get_stats(self):
        self.plan_service.add_course("MAA6")
        self.plan_service.add_course("EG3", "Egen kurs", 8, False)
        self.assertIn("Total credits: 11", self.plan_service.print_stats())
