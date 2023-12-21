import unittest
from services.user_service import UserService

from init_database import initialize_database


class TestUserService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        self.user_service = UserService()

    def test_login_without_account_impossible(self):
        self.assertFalse(self.user_service.login("ParasTili123"))

    def test_current_user_doesnt_exist_without_login(self):
        self.assertFalse(self.user_service.get_current_username())

    def test_creating_user_works(self):
        self.assertTrue(self.user_service.create_user("MinunKäyttäjä"))

    def test_cannot_create_two_times_same_user(self):
        self.assertTrue(self.user_service.create_user("OmaTili1"))
        self.assertFalse(self.user_service.create_user("OmaTili1"))

    def test_login_work_when_account_created(self):
        self.user_service.create_user("KäyttäjäTunnus")
        self.assertTrue(self.user_service.login("KäyttäjäTunnus"))

    def test_when_logged_in_current_user_exist(self):
        self.user_service.create_user("Käyttäjä88")
        self.assertTrue(self.user_service.login("Käyttäjä88"))

        self.assertEqual(
            self.user_service.get_current_username(), "Käyttäjä88")

    def test_loggout_works(self):
        self.user_service.create_user("Paavo666")
        self.assertTrue(self.user_service.login("Paavo666"))

        self.assertEqual(self.user_service.get_current_username(), "Paavo666")

        self.user_service.logout()

        self.assertFalse(self.user_service.get_current_username())
