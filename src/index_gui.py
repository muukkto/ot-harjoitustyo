from tkinter import Tk
from ui.gui.ui import UI


def main():
    window = Tk()
    window.title("Study plan recorder & validator")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()