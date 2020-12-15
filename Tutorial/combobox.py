from tkinter import *
from tkinter.ttk import *

class gui:

    def __init__(self):
        self.windows = Tk()
        self.windows.title("Hello ")
        self.windows.geometry('400x200')

    def combo(self):
        combo = Combobox(self.windows)
        combo['values']=(1, 2, 3, 4, 5, "Text")
        combo.current(1)
        combo.grid(column=0, row=0)
    
    def main(self):
        self.combo()
        self.windows.mainloop()

if __name__ == "__main__":
    a = gui()
    a.main()