from repositories import plan_repository


class UserService:
    def __init__(self):
        self._user = None

    def login(self, username):
        if plan_repository.find_user(username):
            self._user = username
            return username

        return None

    def logout(self):
        self._user = None

    def create_user(self, username):
        if plan_repository.find_user(username):
            return None

        user = plan_repository.create_user(username)
        self._user = user

        return user

    def get_current_user(self):
        return self._user
