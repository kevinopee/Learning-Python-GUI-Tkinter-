from tkinter import *

windows = Tk()
windows.title("Kevin")
windows.geometry('350x200')

label = Label(windows, text="Hello!", font=("Arial Bold", 10), fg="orange")
label.grid(row=0, column=0)

txt = Entry(windows, width=10, state='disabled')
txt.grid(row=0, column=1)
txt.focus()

def clicked():
    res = "Hello " + txt.get()
    label.configure(text=res)

button = Button(windows, text="Click", bg="black", fg="orange", command=clicked)
button.grid(row=0, column=2)

windows.mainloop()