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
