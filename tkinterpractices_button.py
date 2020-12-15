from tkinter import *
# importing the tkinter object
root = Tk()

def my_click():
    my_label = Label(root, text="Click the submit button!")
    my_label.pack()

# command is for calling the my_click object
# so whenever you click that button ass,
# the command tell the my_click to do hit that ass
# fg stands for foreground color, bg stands for background color
myButton = Button(root, text="Submit", command=my_click, padx=5, pady=5, fg="white", bg="#E1C699")
myButton.pack()

root.mainloop()