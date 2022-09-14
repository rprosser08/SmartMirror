from tkinter import *
import DateAndTime, Weather

class MainFrame:
    def __init__(self, master):
        self.master = master

        # create the date and time label
        self.initDateAndTime()

        # create the weather label
        self.initWeather()

    # instantiate the time and date
    def initDateAndTime(self):
        DateAndTime.DateAndTime(self, root)

    def initWeather(self):
        Weather.Weather(self, root)

    def setLocationData(cityString, stateString, zipString, countryString):
        global city, state, zip, country
        city = cityString
        state = stateString
        zip = zipString
        country = countryString


    def getLocationData():
        global city, state, zip, country
        locationData = {
            "city": city,
            "state": state,
            "zip": zip,
            "country": country
        }
        return locationData

def main(cityString, stateString, zipString, countryString):
    global root
    root = Tk()

    root.title("Smart Mirror")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    # MainFrame(root)
    MainFrame.setLocationData(cityString, stateString, zipString, countryString)
    MainFrame(root)
    # Weather.Weather.getHourlyWeather()

    root.mainloop()