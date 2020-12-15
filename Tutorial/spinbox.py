from tkinter import *

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title('Kevin')
        self.windows.geometry('350x200')

    def object_name(self):
        # Object action
        spin = Spinbox(self.windows, from_=0, to=100, width=5)
        spin.grid(row=0, column=0)
        spin2 = Spinbox(self.windows, values=(1, 10, 100), width=5)
        spin2.grid(row=1, column=0)
        var = IntVar()
        var.set(36)
        spin3 = Spinbox(self.windows, from_=0, to=100, width=5, textvar=var)
        spin3.grid(row=2, column=0)


    def main(self):
        # Main action
        self.object_name()
        self.windows.mainloop()

if __name__ == "__main__":
    a = classname()
    a.main()