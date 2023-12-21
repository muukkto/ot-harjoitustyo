from tkinter import Tk, messagebox
from ui.gui.ui import UI

from exceptions import ConfigError


def main():
    """Käynnistää graafisen käyttöliittymän

    Mikäli käynnistyksen yhteydessä nousee "ConfigError"-virhe, ohjelma esittää virheilmoituksen.

    """
    window = Tk()
    window.title("Study plan recorder & validator")

    try:
        ui_view = UI(window)
    except ConfigError:
        messagebox.showerror("Invalid config", "Problems with config files!")
        return

    ui_view.start()
    window.mainloop()


if __name__ == "__main__":
    main()
