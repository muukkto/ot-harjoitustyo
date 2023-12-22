from tkinter import ttk
import tkinter as tk


class CreateUserView:
    """Luokka joka vastaa uuden käyttäjän luomisen graafisesta käyttöliittumästä

    Attributes:
        root: Juuriobjekti, jonka sisälle asetetaan kaikki Tkinter-objektit.
        user_service: Kirjautumisesta vastaava luokka.
        plan_service: Suunnitelman hallinnasta vastaava luokka.
        plan_view: Funktio joka suoritetaan kun halutaan siirtyä suunnitelman päänäkymään.
        login_view: Funktio joka suoritetaan kun halutaan siirtyä kirjautumisnäkymään.
    """
    def __init__(self, root, user_service, plan_service, plan_view, login_view):
        self._root = root
        self._user_service = user_service
        self._plan_service = plan_service
        self._plan_view = plan_view
        self._login_view = login_view

        self._frame = None
        self._username_entry = None

        self._error_text = None
        self._error_label = None

        self._create_view()

    def destroy(self):
        """Funktio piilottaa käyttäjän luomisen näkymän
        """
        self._frame.destroy()

    def _show_error(self, message):
        self._error_text.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _signup_method(self):
        username = self._username_entry.get()

        if username:
            if self._user_service.create_user(username):
                self._plan_service.create_empty_plan_for_user()
                self._plan_view()
            else:
                self._show_error("Couldn't create user!")
        else:
            self._show_error("Couldn't create user!")

    def _create_view(self):
        self._frame = ttk.Frame(self._root)

        self._error_text = tk.StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_text,
            foreground="red"
        )

        self._error_label.grid(row=1, column=0, columnspan=2)

        heading_label = ttk.Label(master=self._frame, text="Create new user")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        button_signup = ttk.Button(
            master=self._frame, text="Create user", command=self._signup_method)
        button_login = ttk.Button(
            master=self._frame, text="Login", command=self._login_view)

        heading_label.grid(row=0, column=0, columnspan=2)
        username_label.grid(row=2, column=0)
        self._username_entry.grid(row=2, column=1)
        button_signup.grid(row=3, column=0, columnspan=2)
        button_login.grid(row=4, column=0, columnspan=2)

        self._hide_error()

        self._frame.grid(column=0, row=0)
