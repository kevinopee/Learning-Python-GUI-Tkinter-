from tkinter import *
from tkinter.ttk import *

class gui:

    def __init__(self):
        self.windows = Tk()
        self.windows.title("Kevin")
        self.windows.geometry("400x200")

    def check(self):
        chk_state = BooleanVar()
        chk_state.set(False) # set check state
        chk = Checkbutton(self.windows, text="Choose", var=chk_state)
        chk.grid(column=0, row=0)

    def main(self):
        self.check()
        self.windows.mainloop()

if __name__ == "__main__":
    a = gui()
    a.main()