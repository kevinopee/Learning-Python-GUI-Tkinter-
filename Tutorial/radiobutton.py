from tkinter import *
from tkinter.ttk import *

class gui:

    def __init__(self):
        self.windows = Tk()
        self.windows.title("Kevin")
        self.windows.geometry('400x200')
    
    def radbut(self):
        rad = Radiobutton(self.windows, text='First', value=1)
        rad2 = Radiobutton(self.windows, text='Second', value=2)
        rad3 = Radiobutton(self.windows, text='Third', value=3)
        rad.grid(row=0, column=0)
        rad2.grid(row=0, column=1)
        rad3.grid(row=0, column=2)

    # def clicked(self):
        # Do what you need

    def main(self):
        self.radbut()
        self.windows.mainloop()

if __name__ == "__main__":
    a = gui()
    a.main() 