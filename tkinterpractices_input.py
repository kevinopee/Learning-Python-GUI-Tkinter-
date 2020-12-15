from tkinter import *

root = Tk()

# Entry() will output the input value from user
#(parameters) contains tkinter objects, width, bg,fg etc
e = Entry(root, width=25, bg="blue")
e.pack()

def my_click():
    my_label = Label(root, text="You've clicked that submit ass")
    my_label.pack()

my_button = Button(root, text="Submit", command=my_click, fg="red", bg="black")
my_button.pack()

root.mainloop()