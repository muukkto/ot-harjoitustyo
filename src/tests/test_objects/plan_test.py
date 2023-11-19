import unittest
from objects.plan import Plan
from objects.curriculum import Curriculum

from config.lops21_curriculum import lops21_curriculum


class TestPlan(unittest.TestCase):
    def setUp(self):
        curriculum = Curriculum(lops21_curriculum())
        self.plan = Plan(curriculum)

    def test_no_courses_exist_at_start(self):
        self.assertEqual(len(self.plan.get_courses_on_plan()), 0)
        self.assertEqual(self.plan.check_if_course_on_plan("HI1"), False)

    def test_unknown_courses_doesnt_exist(self):
        self.assertEqual(self.plan.check_if_course_on_plan("UN1"), False)

    def test_adding_curriculum_courses_work_1(self):
        self.plan.add_curriculum_course_to_plan("MAA12")
        self.assertEqual(self.plan.check_if_course_on_plan("MAA12"), True)
        self.assertEqual(len(self.plan.get_courses_on_plan()), 1)

    def test_adding_curriculum_courses_work_2(self):
        self.plan.add_curriculum_course_to_plan("AI2")
        self.plan.add_curriculum_course_to_plan("AI3")
        self.assertEqual(self.plan.check_if_course_on_plan("AI2"), True)
        self.assertEqual(self.plan.check_if_course_on_plan("AI3"), True)
        self.assertEqual(len(self.plan.get_courses_on_plan()), 2)
    
    def test_adding_curriculum_courses_work_3(self):
        self.plan.add_curriculum_course_to_plan("PS02")
        self.assertEqual(self.plan.check_if_course_on_plan("PS02"), True)
        self.assertEqual(len(self.plan.get_courses_on_plan()), 1)

    def test_adding_own_courses_work_1(self):
        self.plan.add_own_course_to_plan("OMA1", "Oma kurssi", 4)
        self.assertEqual(self.plan.check_if_course_on_plan("OMA1"), True)
        self.assertEqual(len(self.plan.get_courses_on_plan()), 1)

    def test_deleting_courses_work_1(self):
        self.plan.add_curriculum_course_to_plan("KE3")
        self.assertEqual(self.plan.check_if_course_on_plan("KE3"), True)
        self.plan.delete_course_from_plan("KE3")
        self.assertEqual(self.plan.check_if_course_on_plan("KE3"), False)
        self.assertEqual(len(self.plan.get_courses_on_plan()), 0)

    def test_deleting_courses_work_2(self):
        self.plan.add_own_course_to_plan("OMA1", "Oma kurssi", 4)
        self.assertEqual(self.plan.check_if_course_on_plan("OMA1"), True)
        self.plan.delete_course_from_plan("OMA1")
        self.assertEqual(self.plan.check_if_course_on_plan("OMA1"), False)
        self.assertEqual(len(self.plan.get_courses_on_plan()), 0)

    def test_adding_curriculum_course_return_true_if_working_course(self):
        self.assertEqual(self.plan.add_curriculum_course_to_plan("ENA4"), True)

    def test_adding_curriculum_course_return_false_if_broken_course_1(self):
        self.assertEqual(
            self.plan.add_curriculum_course_to_plan("HÖH6"), False)

    def test_adding_curriculum_course_return_false_if_broken_course_2(self):
        self.assertEqual(
            self.plan.add_curriculum_course_to_plan("AI18"), False)

    def test_adding_own_course_return_true_if_working_course(self):
        self.assertEqual(self.plan.add_own_course_to_plan(
            "EI2", "Muu kurssi", 5), True)

    def test_cannot_add_own_course_with_curriculum_code(self):
        self.assertEqual(self.plan.add_own_course_to_plan(
            "BI9", "Biologian kertauskurssi", 2), False)

    def test_deleting_course_return_true_if_working_course(self):
        self.plan.add_curriculum_course_to_plan("FI1")
        self.assertEqual(self.plan.delete_course_from_plan("FI1"), True)

    def test_adding_curriculum_course_return_false_if_broken_course(self):
        self.assertEqual(self.plan.delete_course_from_plan("HÄH2"), False)

    def test_get_correct_total_credits_1(self):
        self.plan.add_curriculum_course_to_plan("FI1")
        self.plan.add_curriculum_course_to_plan("MAA2")
        self.plan.add_curriculum_course_to_plan("MAA4")

        self.assertEqual(self.plan.get_total_credits_on_plan(), 8)
