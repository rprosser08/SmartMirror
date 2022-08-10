from logging import root
from tkinter import *
from datetime import date, datetime
import tkinter

class DateAndTime:
    def __init__(self, master, root):
        self.master = master
        self.createLabel(root)
        self.createUI()

    # Returns the current date
    def getDate():
        return date.today().strftime("%A, %B %d, %Y")

    # Returns the current time
    def getTime():
        return datetime.now().strftime("%I:%M:%S %p")

    # Creates the time and date label
    def createLabel(self, root):
        global clockLabel
        clockLabel = tkinter.Label(root, bg="black", fg="white", font=("Arial", 25))
        clockLabel.place(relx=0.0, rely=0.0, anchor=NW)
        clockLabel.after(0, self.createUI)

    # Updates the time and date label every half second
    def createUI(self):
        clockLabel.configure(text=DateAndTime.getTime() + "\n" + DateAndTime.getDate())
        clockLabel.after(500, self.createUI)
