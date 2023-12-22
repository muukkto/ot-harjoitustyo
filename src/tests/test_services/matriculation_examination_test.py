import unittest
from objects.plan import Plan
from objects.curriculum import Curriculum

from services.validation.meb_validation_service import MebValidationService

from config.config import CURRICULUM


class TestMebPlan(unittest.TestCase):
    def setUp(self):
        curriculum = Curriculum(CURRICULUM)
        self.plan = Plan(curriculum, "User1")
        self.validation = MebValidationService()

    def test_adding_subject_to_meb_plan_1(self):
        self.plan.add_exam_to_meb_plan("BI", 1)
        self.plan.add_exam_to_meb_plan("YH", 2)
        self.assertCountEqual(
            self.plan.return_exams_in_meb_plan(), ["BI", "YH"])

    def test_adding_subject_to_meb_plan_2(self):
        self.assertTrue(self.plan.add_exam_to_meb_plan("FF", 3))

    def test_removing_subject_from_me_plan(self):
        self.plan.add_exam_to_meb_plan("M", 1)
        self.plan.add_exam_to_meb_plan("EA", 2)
        self.assertCountEqual(
            self.plan.return_exams_in_meb_plan(), ["M", "EA"])

        self.plan.remove_exam_from_meb_plan("EA", 2)
        self.assertCountEqual(self.plan.return_exams_in_meb_plan(), ["M"])

    def test_cannot_add_illegal_subjects_1(self):
        self.plan.add_exam_to_meb_plan("BIO", 3)
        self.assertEqual(self.plan.return_exams_in_meb_plan(), [])

    def test_cannot_add_illegal_subjects_2(self):
        self.assertFalse(self.plan.add_exam_to_meb_plan("EAB", 2))

    def test_cannot_remove_illegal_time(self):
        self.assertFalse(self.plan.remove_exam_from_meb_plan("BB", 7))

    def test_cannot_add_subjects_with_illegal_period(self):
        self.plan.add_exam_to_meb_plan("A", 6)
        self.assertEqual(self.plan.return_exams_in_meb_plan(), [])

    def test_validate_legal_plan(self):
        self.plan.add_exam_to_meb_plan("A", 1)
        self.plan.add_exam_to_meb_plan("EA", 1)
        self.plan.add_exam_to_meb_plan("N", 2)
        self.plan.add_exam_to_meb_plan("GE", 3)
        self.plan.add_exam_to_meb_plan("FY", 3)

        self.assertFalse(self.validation.validate(self.plan))

    def test_validate_illegal_plan_structure(self):
        self.plan.add_exam_to_meb_plan("A", 1)
        self.plan.add_exam_to_meb_plan("EC", 1)
        self.plan.add_exam_to_meb_plan("GE", 3)
        self.plan.add_exam_to_meb_plan("FY", 3)
        self.plan.add_exam_to_meb_plan("HI", 2)

        self.assertTrue(self.validation.validate(self.plan))

    def test_validate_illegal_plan_timing(self):
        self.plan.add_exam_to_meb_plan("A", 1)
        self.plan.add_exam_to_meb_plan("EC", 1)
        self.plan.add_exam_to_meb_plan("GE", 3)
        self.plan.add_exam_to_meb_plan("YH", 3)
        self.plan.add_exam_to_meb_plan("A", 2)

        self.assertTrue(self.validation.validate(self.plan))

    def test_validate_empty_plan(self):
        self.assertTrue(self.validation.validate(self.plan))
