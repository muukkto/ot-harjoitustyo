from services.user_service import UserService
from services.plan_service import PlanService

from ui.gui.views.login_view import LoginView
from ui.gui.views.plan_view import PlanView
from ui.gui.views.create_user_view import CreateUserView


class UI:
    def __init__(self, root):
        self._root = root
        self._root.rowconfigure(0, weight=1)
        self._current_view = None
        self._user_service = UserService()
        self._plan_service = PlanService(self._user_service)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def start(self):
        self._show_login_view()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(self._root,
                                       self._user_service,
                                       self._plan_service,
                                       self._show_plan_view,
                                       self._show_create_user_view)

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(self._root,
                                            self._user_service,
                                            self._plan_service,
                                            self._show_plan_view,
                                            self._show_login_view)

    def _show_plan_view(self):
        self._hide_current_view()

        self._current_view = PlanView(self._root,
                                      self._plan_service,
                                      self._user_service,
                                      self._show_login_view)
