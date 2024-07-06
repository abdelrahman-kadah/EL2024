"""
Write a program in Python that displays a window to the user that asks them to enter an integer
N and displays its factorial
"""


from tkinter import *

mainWindow = Tk()


number = IntVar()
result = StringVar()


def factorial():
    global number
    global result

    fact = 1
    for i in range(number.get(), 1, -1):
        fact *= i

    result.set(f"The Factorial of {number.get()} is {number.get()}! = {fact}")



Label(mainWindow, text="Enter the value of N: ").grid(row=0, column=0, padx=30, pady=20)
Entry(mainWindow, width=30, textvariable=number).grid(row=0, column=1, padx=50, pady=20)

Label(mainWindow, textvariable=result).grid(row=1, column=1)
Button(mainWindow, text="Factorial", command=factorial).grid(row=2, column=1)

mainWindow.mainloop()
