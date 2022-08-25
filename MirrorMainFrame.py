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
        global city, state, country
        city = cityString
        state = stateString
        country = countryString

    def getLocationData():
        global city, state, country
        locationData = {
            "city": city,
            "state": state,
            "country": country
        }
        return locationData

def main(cityString, stateString, countryString):
    global root
    root = Tk()

    root.title("Smart Mirror")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    MainFrame(root)
    MainFrame.setLocationData(cityString, stateString, countryString)
    Weather.WebScraper.getURL()

    root.mainloop()