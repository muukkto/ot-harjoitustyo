from repositories.plan_repository import PlanRepository

class UserService:
    def __init__(self):
        self._user = None

    def login(self, username):
        if PlanRepository().find_user(username):
            self._user = username
            return username

        return None

    def logout(self):
        self._user = None

    def create_user(self, username):
        if PlanRepository().find_user(username):
            return None

        user = PlanRepository().create_user(username)
        self._user = user

        return user

    def get_current_user(self):
        return self._user
