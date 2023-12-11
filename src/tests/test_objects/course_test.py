import unittest

from objects.course import Course


class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("MAA12", "MAA")

    def test_course_status_can_be_changed_on_plan(self):
        self.course.change_status(True)
        self.assertEqual(self.course.status(), True)

    def test_course_status_can_be_changed_off_plan(self):
        self.course.change_status(False)
        self.assertEqual(self.course.status(), False)

    def test_course_prints_name(self):
        self.assertEqual(str(self.course), "MAA12")

    def test_curriculum_course_doesnt_return_ects(self):
        self.assertEqual(self.course.get_ects(), None)

    def test_own_course_return_ects(self):
        course = Course("OMA1", on_cur=False, name="Oma kurssi 1", ects=2)
        self.assertEqual(course.get_ects(), 2)
