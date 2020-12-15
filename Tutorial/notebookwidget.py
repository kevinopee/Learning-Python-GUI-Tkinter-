from tkinter import *
from tkinter import ttk

class gui:
    def __init__(self):
        self.windows = Tk()
        self.windows.title('Apa')
        self.windows.geometry('500x250')
    
    def tab(self):
        self.tab_control = ttk.Notebook(self.windows)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='First')
        self.tab_control.add(self.tab2, text='Second')
        

    def labels(self):
        lbl1 = Label(self.tab1, text='Label 1', padx=5, pady=5)
        lbl1.grid(row=0, column=0)
        lbl2 = Label(self.tab2, text='Label 2', padx=5, pady=5)
        lbl2.grid(row=0, column=0)
        self.tab_control.pack(expand=1, fill='both')
    
    def main(self):
        self.tab()
        self.labels()
        self.windows.mainloop()

if __name__ == "__main__":
    a = gui()
    a.main()