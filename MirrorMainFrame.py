from tkinter import *
import DateAndTime, Weather, Calendar

class MainFrame:
    def __init__(self, master):
        self.master = master

        # create the date and time label
        self.initDateAndTime()

        # create the weather label
        self.initWeather()

        self.initCalendar()

    # instantiate the time and date
    def initDateAndTime(self):
        DateAndTime.DateAndTime(self, root)

    def initWeather(self):
        Weather.Weather(self, root)

    def initCalendar(self):
        Calendar.Calendar(self, root)

    def setLocationData(zipString):
        global zip
        zip = zipString


    def getLocationData():
        global zip
        locationData = {
            "zip": zip
        }
        return locationData

def main(zipString):
    global root
    root = Tk()

    root.title("Smart Mirror")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    # MainFrame(root)
    MainFrame.setLocationData(zipString)
    MainFrame(root)
    # Weather.Weather.getHourlyWeather()

    root.mainloop()