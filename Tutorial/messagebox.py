from tkinter import *
from tkinter import messagebox

class classname:

    def __init__(self):
        # Main Constructor
        self.windows = Tk()
        self.windows.title("Kevin")
        self.windows.geometry('350x200')

    def object_name(self):
        # Object action
        messagebox.showinfo('Lol', 'Kontol')
        messagebox.showwarning('Peler', 'Wkwkw')
        messagebox.showerror('Haha', 'haha')
        messagebox.askquestion('Message title','Message content')
        messagebox.askyesno('Message title','Message content')
        messagebox.askyesnocancel('Message title','Message content')
        messagebox.askokcancel('Message title','Message content')
        messagebox.askretrycancel('Message title','Message content')

    def btn(self):
        btn = Button(self.windows, text='Click', command=self.object_name)
        btn.grid(row=0, column=0)

    def main(self):
        # Main action
        self.btn()
        self.windows.mainloop()

if __name__ == "__main__":
    a = classname()
    a.main()