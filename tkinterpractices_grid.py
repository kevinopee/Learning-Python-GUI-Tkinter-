from tkinter import *
# importing the tkinter object
root = Tk()

# create a label widget
myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Kevin Christopher")
myLabel3 = Label(root, text="My Name is Kevin Christopher")
# shoving it onto the screen

myLabel.grid(row=0, column=0) 
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)

root.mainloop()