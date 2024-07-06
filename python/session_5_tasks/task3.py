"""
Create a graphical application in Python Tkinter that asks
the user to enter two integers and displays their sum
"""

from tkinter import *

mainWindow = Tk()


number1 = IntVar()
number2 = IntVar()
result = StringVar()


def sum():
    global number1
    global number2
    global result

    result.set(f"The Sum is: {number1.get()} + {number2.get()} = {number1.get() + number2.get()}")
    number1.set('')
    number2.set('')

Label(mainWindow, text="Enter the value of M: ").grid(row=0, column=0, padx=30, pady=20)
Entry(mainWindow, width=30, textvariable=number1).grid(row=0, column=1, padx=50, pady=20)

Label(mainWindow, text="Enter the value of N: ").grid(row=1, column=0, padx=30, pady=20)
Entry(mainWindow, width=30, textvariable=number2).grid(row=1, column=1, padx=50, pady=20)

Label(mainWindow, textvariable=result).grid(row=2, column=1)
Button(mainWindow, text="Sum", command=sum).grid(row=3, column=1)

mainWindow.mainloop()
