"""
Write a program that asks the user to type word and return him its reverse
"""

from tkinter import *

mainWindow = Tk()

normalText = StringVar()
reversedText = StringVar()


def reverseWord():
    global normalText
    global reversedText
    reversedText.set(normalText.get()[::-1])

Label(mainWindow, text="Enter a word:").grid(row=0, column=0, padx=30, pady=20)
Entry(mainWindow, width=30, textvariable=normalText).grid(row=0, column=1, padx=50, pady=20)
Label(mainWindow, textvariable=reversedText).grid(row=1, column=1)
Button(mainWindow, text="Reverse", command=reverseWord).grid(row=2, column=1)

mainWindow.mainloop()
