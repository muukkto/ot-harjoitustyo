from tkinter import filedialog as fd 

def open_file():

    filetypes = (('Plan file (*.json)', '*.json'),)

    return fd.asksaveasfile(mode='w', filetypes=filetypes, initialdir="C:/")

#f = fd.askopenfile(filetypes=filetypes, initialdir="D:/Downloads")

print(open_file())