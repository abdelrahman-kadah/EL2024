from tkinter import *

mainWindow = Tk()
mainWindow.geometry("200x200")


lbl_text = StringVar()

def ledOn():
    my_canvas.itemconfig(my_oval, fill="red")
    lbl_text.set("Led is on.")
    

def ledOff():
    my_canvas.itemconfig(my_oval, fill="white")
    lbl_text.set("Led is off.")
    



my_canvas = Canvas(mainWindow, width=100, height=100)

my_oval = my_canvas.create_oval(25, 25, 80, 80, fill="white")

my_canvas.pack()

Label(mainWindow, width=50, textvariable=lbl_text).pack()
Button(mainWindow, text="Led OFF", command=ledOff).pack()
Button(mainWindow, text="Led ON", command=ledOn).pack()




mainWindow.mainloop()