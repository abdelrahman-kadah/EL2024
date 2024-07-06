"""
Make a GUI template (In the slides) and each button displays different name
"""

from tkinter import *

mainWindow = Tk()

# mainWindow.geometry("450x450+450+450")

mainWindow.resizable(0, 0)

def sayHello():
    print("Hello")

def sayHi():
    print("Hi")

def sayWelcome():
    print("Welcome")

def sayAloha():
    print("Aloha")

Button(mainWindow, command=sayHello, text="Button 1").grid(row=0, column=1)
Button(mainWindow, command=sayHi, text="Button 2").grid(row=1, column=0)
Button(mainWindow, command=sayWelcome, text="Button 3").grid(row=1, column=2)
Button(mainWindow, command=sayAloha, text="Button 4").grid(row=2, column=1)


mainWindow.mainloop()