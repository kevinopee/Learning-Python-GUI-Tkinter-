from tkinter import filedialog
from tkinter import *
from os import path

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title('Kevin')
        self.windows.geometry('350x200')

    def object_name(self):
        # Object action
        file = filedialog.askopenfilename(filetypes= (('Text files', '*.txt'),("all files","*.*")))
        dir = filedialog.askdirectory()
        filee = filedialog.askopenfilename(initialdir=path.dirname(__file__))

    def main(self):
        # Main action
        self.object_name()
        self.windows.mainloop()


if __name__ == "__main__":
    a = classname()
    a.main()