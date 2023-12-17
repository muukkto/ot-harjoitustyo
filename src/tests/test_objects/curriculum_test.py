import unittest
from objects.curriculum import Curriculum

from config.config import CURRICULUM


class TestCurriculum(unittest.TestCase):
    def setUp(self):
        self.curriculum = Curriculum(CURRICULUM)

    def test_curriculum_exports_subject_codes(self):
        self.assertIn("AI", self.curriculum.return_all_subject_codes())
        self.assertIn("RUB", self.curriculum.return_all_subject_codes())

    def test_curriculum_get_subject_code_from_course_code(self):
        self.assertEqual(
            self.curriculum.get_subject_code_from_course_code("BI2"), "BI")
        self.assertEqual(
            self.curriculum.get_subject_code_from_course_code("KU4"), "KU")

    def test_curriculum_cannot_get_subject_code_from_broken_course_code(self):
        self.assertEqual(
            self.curriculum.get_subject_code_from_course_code("TÄH7"), None)

    def test_get_credits_from_subject_code(self):
        self.assertEqual(
            self.curriculum.get_credits_from_course_code("MAA2"), 3)
        self.assertEqual(
            self.curriculum.get_credits_from_course_code("AI2"), 1)
        self.assertEqual(
            self.curriculum.get_credits_from_course_code("MU2"), 2)
        self.assertEqual(
            self.curriculum.get_credits_from_course_code("RUB4"), 2)

    def test_get_mandatory_credits(self):
        self.assertEqual(
            self.curriculum.get_mandatory_credits_subject("AI"), 12)
        self.assertEqual(
            self.curriculum.get_mandatory_credits_subject("BI"), 4)
        self.assertEqual(
            self.curriculum.get_mandatory_credits_subject("MAA"), 20)
