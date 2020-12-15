from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title('Kevin')
        self.windows.geometry('350x200')

    def object_name(self):
        # Object action
        style = ttk.Style()
        style.theme_use('default')
        style.configure('black.Horizontal.TProgresbar', background='black')

    def bar_progress(self):
        bar = Progressbar(self.windows, length=100, style='black.Horizontal.TProgressbar')
        bar['value'] = 70
        bar.grid(row=0, column=0)

    def main(self):
        # Main action
        self.object_name()
        self.bar_progress()
        self.windows.mainloop()

if __name__ == "__main__":
    a = classname()
    a.main()