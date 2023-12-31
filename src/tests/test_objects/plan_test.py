import unittest
from objects.plan import Plan
from objects.curriculum import Curriculum

from config.config import CURRICULUM


class TestPlan(unittest.TestCase):
    def setUp(self):
        curriculum = Curriculum(CURRICULUM)
        self.plan = Plan(curriculum, "User1")

    def test_no_courses_exist_at_start(self):
        self.assertEqual(len(self.plan.get_courses_on_plan()), 0)
        self.assertFalse(self.plan.check_if_course_on_plan("HI1"))

    def test_unknown_courses_doesnt_exist(self):
        self.assertFalse(self.plan.check_if_course_on_plan("UN1"))

    def test_adding_curriculum_courses_work_1(self):
        self.plan.add_course_to_plan("MAA12", on_cur=True)
        self.assertTrue(self.plan.check_if_course_on_plan("MAA12"))
        self.assertEqual(len(self.plan.get_courses_on_plan()), 1)

    def test_adding_curriculum_courses_work_2(self):
        self.plan.add_course_to_plan("AI2", on_cur=True)
        self.plan.add_course_to_plan("AI3", on_cur=True)
        self.assertTrue(self.plan.check_if_course_on_plan("AI2"))
        self.assertTrue(self.plan.check_if_course_on_plan("AI3"))
        self.assertEqual(len(self.plan.get_courses_on_plan()), 2)

    def test_adding_curriculum_courses_work_3(self):
        self.plan.add_course_to_plan("PS2", on_cur=True)
        self.assertTrue(self.plan.check_if_course_on_plan("PS2"))
        self.assertEqual(len(self.plan.get_courses_on_plan()), 1)

    def test_adding_own_courses_work_1(self):
        self.plan.add_course_to_plan("OMA1", "Oma kurssi", 4, on_cur=False)
        self.assertTrue(self.plan.check_if_course_on_plan("OMA1"))
        self.assertEqual(len(self.plan.get_courses_on_plan()), 1)

    def test_deleting_courses_work_1(self):
        self.plan.add_course_to_plan("KE3", on_cur=True)
        self.assertTrue(self.plan.check_if_course_on_plan("KE3"))
        self.plan.delete_course_from_plan("KE3")
        self.assertFalse(self.plan.check_if_course_on_plan("KE3"))
        self.assertEqual(len(self.plan.get_courses_on_plan()), 0)

    def test_deleting_courses_work_2(self):
        self.plan.add_course_to_plan("OMA1", "Oma kurssi", 4, on_cur=False)
        self.assertTrue(self.plan.check_if_course_on_plan("OMA1"))
        self.plan.delete_course_from_plan("OMA1")
        self.assertFalse(self.plan.check_if_course_on_plan("OMA1"))
        self.assertEqual(len(self.plan.get_courses_on_plan()), 0)

    def test_adding_curriculum_course_return_true_if_working_course(self):
        self.assertTrue(self.plan.add_course_to_plan("ENA4", on_cur=True))

    def test_adding_curriculum_course_return_false_if_broken_course_1(self):
        self.assertFalse(
            self.plan.add_course_to_plan("HÖH6", on_cur=True))

    def test_adding_curriculum_course_return_false_if_broken_course_2(self):
        self.assertFalse(
            self.plan.add_course_to_plan("AI18", on_cur=True))

    def test_adding_own_course_return_true_if_working_course(self):
        self.assertTrue(self.plan.add_course_to_plan(
            "EI2", "Muu kurssi", 5, on_cur=False))

    def test_cannot_add_own_course_with_curriculum_code(self):
        self.assertFalse(self.plan.add_course_to_plan(
            "BI9", "Biologian kertauskurssi", 2, on_cur=False))

    def test_cannot_add_own_course_two_times_same_code(self):
        self.plan.add_course_to_plan("OMA1", "Oma kurssi 1", 2, on_cur=False)
        self.assertFalse(self.plan.add_course_to_plan(
            "OMA1", "Toinen oma kurssi", 2, on_cur=False))

    def test_deleting_course_return_true_if_working_course(self):
        self.plan.add_course_to_plan("FI1", on_cur=True)
        self.assertTrue(self.plan.delete_course_from_plan("FI1"))

    def test_adding_curriculum_course_return_false_if_broken_course(self):
        self.assertFalse(self.plan.delete_course_from_plan("HÄH2"))

    def test_get_correct_total_credits_1(self):
        self.plan.add_course_to_plan("FI1", on_cur=True)
        self.plan.add_course_to_plan("MAA2", on_cur=True)
        self.plan.add_course_to_plan("MAA4", on_cur=True)

        self.assertEqual(self.plan.get_total_credits_on_plan(), 8)

    def test_change_mab_language_to_swedish(self):
        self.assertTrue(self.plan.change_meb_language("sv"))

    def test_change_meb_language_to_france_doesnt_work(self):
        self.assertFalse(self.plan.change_meb_language("fr"))

    def test_change_graduation_period_works_with_legal_input(self):
        self.assertTrue(self.plan.change_graduation_period("2025K"))

    def test_change_graduation_period_doesnt_work_with_illegal_input(self):
        self.assertFalse(self.plan.change_graduation_period("2023U"))
