import unittest

from services.validation_service import ValidationService

from objects.curriculum import Curriculum
from objects.plan import Plan

from config.lops21_curriculum import lops21_curriculum


class TestValidationService(unittest.TestCase):
    def setUp(self):
        self.curriculum = Curriculum(lops21_curriculum())
        self.validation_service = ValidationService()

    def test_validate_legal_plan(self):
        plan = Plan(self.curriculum)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "GE1", "GE3",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "FI2", "PS1", "HI1", "HI2", "HI3", "YH1", "YH2", "YH3",
                         "ET1", "ET2", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertFalse(self.validation_service.validate(
            plan, self.curriculum))

    def test_validate_legal_special_task_plan(self):
        plan = Plan(self.curriculum)
        plan.change_special_task(True)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "GE1", "GE3",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "PS1", "HI1", "HI2", "YH1", "YH2",
                         "ET1", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2",
                         "ERI1", "ERI2", "ERI3", "ERI4", "ERI5", "ERI6", "ERI7", "ERI8", "ERI9", "ERI10", "ERI11", "ERI12"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertFalse(self.validation_service.validate(
            plan, self.curriculum))

    def test_validate_illegal_plan_not_enough_special_task_credits(self):
        plan = Plan(self.curriculum)
        plan.change_special_task(True)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "GE1", "GE3",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "PS1", "HI1", "HI2", "YH1", "YH2",
                         "ET1", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2",
                         "ERI1", "ERI2", "ERI3", "ERI4", "ERI5"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_too_much_excluded(self):
        plan = Plan(self.curriculum)
        plan.change_special_task(True)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA7", "MAA8", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "GE1", "GE3",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "PS1", "HI1", "HI2", "YH1", "YH2",
                         "ET1", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2",
                         "ERI1", "ERI2", "ERI3", "ERI4", "ERI5", "ERI6", "ERI7", "ERI8", "ERI9", "ERI10", "ERI11", "ERI12"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_too_much_excluded_in_basket_subject(self):
        plan = Plan(self.curriculum)
        plan.change_special_task(True)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "GE1", "GE3",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "PS1", "HI1", "HI2", "YH1", "YH2", "YH3",
                         "ET1", "TE1", "TE2", "TE3", "LI1", "LI2", "KU1", "KU2", "OP1", "OP2",
                         "ERI1", "ERI2", "ERI3", "ERI4", "ERI5", "ERI6", "ERI7", "ERI8", "ERI9", "ERI10", "ERI11", "ERI12"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_too_much_excluded_one_subject(self):
        plan = Plan(self.curriculum)
        plan.change_special_task(True)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "PS1", "HI1", "HI2", "HI3", "YH1", "YH2", "YH3"
                         "ET1", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2",
                         "ERI1", "ERI2", "ERI3", "ERI4", "ERI5", "ERI6", "ERI7", "ERI8", "ERI9", "ERI10", "ERI11", "ERI12"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_too_much_excluded_group_subject(self):
        plan = Plan(self.curriculum)
        plan.change_special_task(True)
        legal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                         "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                         "RUB1", "RUB2", "RUA1", "RUA2",
                         "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                         "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                         "GE1", "GE3",
                         "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                         "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                         "FI1", "PS1", "HI1", "HI2", "YH1", "YH2",
                         "ET1", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2",
                         "ERI1", "ERI2", "ERI3", "ERI4", "ERI5", "ERI6", "ERI7", "ERI8", "ERI9", "ERI10", "ERI11", "ERI12"]

        for course in legal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_not_enough_credits(self):
        plan = Plan(self.curriculum)
        illegal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8",
                           "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                           "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                           "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9",
                           "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                           "GE1", "GE3",
                           "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                           "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                           "FI1", "FI2", "PS1", "HI1", "HI2", "HI3", "YH1", "YH2", "YH3",
                           "ET1", "ET2", "TE1", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2"]

        for course in illegal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_not_enough_voluntary_credits(self):
        plan = Plan(self.curriculum)
        illegal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8",
                           "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6",
                           "RUB1", "RUB2", "RUB3", "RUB4", "RUB5",
                           "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9",
                           "BI1", "BI2", "BI3",
                           "GE1",
                           "FY1", "FY2",
                           "KE1", "KE2",
                           "FI1", "FI2", "PS1", "HI1", "HI2", "HI3", "YH1", "YH2", "YH3",
                           "ET1", "ET2", "TE1", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2",
                           "VAPA1", "VAPA2", "VAPA3", "VAPA4", "VAPA5", "VAPA6", "VAPA7", "VAPA8", "VAPA9", "VAPA10",
                           "VAPA11", "VAPA12", "VAPA13", "VAPA14", "VAPA15", "VAPA16", "VAPA17", "VAPA18", "VAPA19", "VAPA20",
                           "VAPA21", "VAPA22", "VAPA23", "VAPA24", "VAPA25"]

        for course in illegal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_not_all_mandatory(self):
        plan = Plan(self.curriculum)
        illegal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI10", "AI11",
                           "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                           "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                           "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                           "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                           "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                           "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                           "FI1", "FI2", "PS1", "HI1", "HI2", "HI3", "HI4", "HI5", "HI6", "YH1", "YH2", "YH3", "YH4",
                           "ET1", "ET2", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "KU2", "OP1", "OP2"]

        for course in illegal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))

    def test_validate_illegal_plan_not_all_mandatory_arts(self):
        plan = Plan(self.curriculum)
        illegal_courses = ["AI1", "AI2", "AI3", "AI4", "AI5", "AI6", "AI7", "AI8", "AI10", "AI11",
                           "ENA1", "ENA2", "ENA3", "ENA4", "ENA5", "ENA6", "ENA8", "ENA7",
                           "RUB1", "RUB2", "RUB3", "RUB4", "RUB5", "RUB7",
                           "MAA1", "MAA2", "MAA3", "MAA4", "MAA5", "MAA6", "MAA7", "MAA8", "MAA9", "MAA10", "MAA11", "MAA12",
                           "BI1", "BI2", "BI3", "BI4", "BI5", "BI6",
                           "GE1", "GE2", "GE3",
                           "FY1", "FY2", "FY3", "FY4", "FY5", "FY6", "FY7", "FY8",
                           "KE1", "KE2", "KE3", "KE4", "KE5", "KE6",
                           "FI1", "FI2", "PS1", "HI1", "HI2", "HI3", "YH1", "YH2", "YH3",
                           "ET1", "ET2", "TE1", "TE2", "TE3", "LI1", "LI2", "MU1", "KU1", "OP1", "OP2"]

        for course in illegal_courses:
            plan.add_curriculum_course_to_plan(course)

        self.assertTrue(
            self.validation_service.validate(plan, self.curriculum))
