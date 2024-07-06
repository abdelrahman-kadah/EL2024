"""
try to make
gauge like pic
"""

from tkinter import *


mainWindow = Tk()

mainWindow.geometry("500x500")

my_canvas = Canvas(mainWindow, width=500, height=500, background="white")

my_canvas.create_text(210, 20, font="Times 20 italic bold", text="Humidity")


my_canvas.create_arc(10, 50, 400, 500, start=70, extent=70, width=40, outline="green", style="arc")
my_canvas.create_arc(10, 50, 400, 500, start=60, extent=20, width=40, outline="yellow", style="arc")
my_canvas.create_arc(10, 50, 400, 500, start=40, extent=20, width=40, outline="red", style="arc")

my_canvas.create_text(40, 150, font="Times 12 bold", text="0")
my_canvas.create_text(360, 150, font="Times 12 bold", text="100")
my_canvas.create_text(215, 260, font="Times 12 bold", text="36%")

my_canvas.create_line(70, 140, 210, 250, fill="black")
my_canvas.create_line(100, 110, 210, 250, fill="black")
my_canvas.create_line(140, 85, 210, 250, fill="black")
my_canvas.create_line(170, 50, 210, 250, width=7, fill="black")
my_canvas.create_line(220, 70, 210, 250, fill="black")
my_canvas.create_line(280, 90, 210, 250, fill="black")
my_canvas.create_line(320, 115, 210, 250, fill="black")
my_canvas.create_line(340, 140, 210, 250, fill="black")

my_canvas.pack()

mainWindow.mainloop()
