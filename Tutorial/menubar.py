from tkinter import *
from tkinter import Menu

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title('Kevin')

    def object_name(self):
        # Object action
        menu = Menu(self.windows)
        new_item = Menu(menu, tearoff=0)
        new_item.add_command(label='New')
        new_item.add_separator()
        new_item.add_command(label='Edit')
        menu.add_cascade(label='File', menu=new_item)
        self.windows.config(menu=menu)

    def main(self):
        # Main action
        self.object_name()
        self.windows.mainloop()

if __name__ == "__main__":
    a = classname()
    a.main()