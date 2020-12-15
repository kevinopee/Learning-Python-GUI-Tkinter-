from tkinter import *
from tkinter.ttk import *

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title("Kevin")

    def radio_button(self):
        # Object action
        self.selected = IntVar()
        rad1 = Radiobutton(self.windows, text='First', value=1, variable=self.selected)
        rad2 = Radiobutton(self.windows, text='Second', value=2, variable=self.selected)
        rad3 = Radiobutton(self.windows, text='Third', value=3, variable=self.selected)
        rad1.grid(row=0, column=0)
        rad2.grid(row=0, column=1)
        rad3.grid(row=0, column=2)

    def click(self):
        print(self.selected.get())

    def button(self):
        btn = Button(self.windows, text="Click", command=self.click)
        btn.grid(row=0, column=3)

    def main(self):
        self.radio_button()
        self.button()
        self.windows.mainloop()

if __name__ == "__main__":
    a = classname()
    a.main()