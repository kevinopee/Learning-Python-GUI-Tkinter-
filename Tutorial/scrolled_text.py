from tkinter import *
from tkinter import scrolledtext

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title("Kevin")
        self.windows.geometry('350x150')
        
    def scrolled_text(self):
        # Object action
        txt = scrolledtext.ScrolledText(self.windows, width=40, height=10)
        txt.grid(row=0, column=0)
        txt.insert(INSERT, 'Hello')
        txt.delete(1.0, END)

    def main(self):
        # Main action
        self.scrolled_text()
        self.windows.mainloop()

if __name__ == "__main__":
    a = classname()
    a.main()