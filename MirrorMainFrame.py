from tkinter import *
import DateAndTime, Weather

class MainFrame:
    def __init__(self, master):
        self.master = master

        # create the date and time label
        self.initDateAndTime()

        # Weather.Weather.getLocation()

    # instantiate the time and date
    def initDateAndTime(self):
        DateAndTime.DateAndTime(self, root)

    def setLocationData(cityString, stateString, countryString):
        print(cityString)
        print(stateString)
        print(countryString)

def main(cityString, stateString, countryString):
    global root
    root = Tk()

    root.title("Smart Mirror")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    MainFrame(root)
    MainFrame.setLocationData(cityString, stateString, countryString)

    root.mainloop()