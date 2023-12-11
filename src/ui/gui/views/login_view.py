from tkinter import ttk
import tkinter as tk


class LoginView:
    def __init__(self, root, user_service, plan_service, plan_view, create_user_view):
        self._root = root
        self._user_service = user_service
        self._plan_service = plan_service
        self._plan_view = plan_view
        self._create_user_view = create_user_view

        self._frame = None
        self._username_entry = None

        self._error_text = None
        self._error_label = None

        self._create_view()

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_text.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _login_method(self):
        username = self._username_entry.get()

        if username:
            if self._user_service.login(username):
                self._plan_service.read_plan_for_user()
                self._plan_view()
            else:
                self._show_error("Username not found!")
        else:
            self._show_error("Username not found!")

    def _create_view(self):
        self._frame = ttk.Frame(self._root)

        self._error_text = tk.StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_text,
            foreground="red"
        )

        self._error_label.grid(row=1, column=0, columnspan=2)

        heading_label = ttk.Label(master=self._frame, text="Login")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        button_login = ttk.Button(
            master=self._frame, text="Login", command=self._login_method)
        button_create_user = ttk.Button(
            master=self._frame, text="Create user", command=self._create_user_view)

        heading_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=2, column=0)
        self._username_entry.grid(row=2, column=1)
        button_login.grid(row=3, column=0, columnspan=2)
        button_create_user.grid(row=4, column=0, columnspan=2)

        self._hide_error()

        self._frame.grid(column=0, row=0)
