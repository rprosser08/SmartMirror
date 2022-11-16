import requests, MirrorMainFrame, re, urllib.request, json
from DateAndTime import DateAndTime
from datetime import datetime
from tkinter import *
import tkinter


class Weather:
    global apiKey, locationSet, key, counter
    locationSet = False
    counter = 0

    def __init__(self, master, root):
        self.master = master
        self.createLabel(root)
        self.createUI()
     
    def getLocation():
        return MirrorMainFrame.MainFrame.getLocationData()

    # Gets the location key from Accuweather needed to get the weather data for the location
    def setLocationKey():
        global apiKey, locationSet, key
        location = Weather.getLocation()
        zipCode = location["zip"]
        URL = "http://dataservice.accuweather.com/locations/v1/postalcodes/US/search?apikey=" + apiKey + "&q=" + zipCode + "&language=en-us&details=true"
        response = requests.get(URL)
        json = response.json()
        key = json[0]["Key"]
        locationSet = True
        return key

    # Gets the 12 - hourly weather data for the location 
    def getHourlyWeather():
        global apiKey, key, locationSet
        Weather.setAPIKey()
        if not locationSet:
            Weather.setLocationKey()
        URL = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + key + "?apikey=" + apiKey + "&language=en-us&details=true&metric=false"
        response = requests.get(URL)
        weatherData = response.json()
        print(weatherData)
        fiveHourData = Weather.formatData(weatherData)
        return fiveHourData

    # Gets the Accuweahter API key from the file "APIKey.txt"
    def setAPIKey():
        global apiKey
        with open("APIKey.txt") as f:
            apiKey = f.read()

    # Stores the first 5 hours of weather data in the formatted data list as individal dictionaries for each hour
    def formatData(weatherDataList):
        formattedData = []

        # Gets the frist 5 hours of weather data into the correct data structures
        for i in range(5):
            # Dictionary to store each data value (Time, Temp, Feel Like Temp, Precipitation Chance)
            dataDictionary = {}

            # Gets the time from the weather data and formats it to 12-hour clock -> 12:00 AM and stores it in the dictionary
            weatherTime = weatherDataList[i]["DateTime"]
            FullTime = weatherTime.split("T")[1]
            _24HrTime = FullTime.split("-")[0]
            time_object = datetime.strptime(_24HrTime, "%H:%M:%S").time()
            time = time_object.strftime("%-I:%M %p")
            dataDictionary.update({"Time": time})

            # Gets the temperature from the weather data and stores it in the dictionary
            temp = int(weatherDataList[i]["Temperature"]["Value"])
            dataDictionary.update({"Temp": str(temp)})

            # Gets the feels like temperature from the weather data and stores it in the dictionary
            feelsTemp = int(weatherDataList[i]["RealFeelTemperature"]["Value"])
            dataDictionary.update({"FeelsTemp": str(feelsTemp)})

            # Gets the chance of percipitation from the weather data and stores it in the dictionary
            precipChance = weatherDataList[i]["PrecipitationProbability"]
            dataDictionary.update({"PrecipChance": str(precipChance)})

            formattedData.append(dataDictionary)
        
        return formattedData

    def formattedWweatherString():
        degreeSymbol = "\u00B0"
        weatherData = Weather.getHourlyWeather()
        print(weatherData)
        hour1 = weatherData[0]["Time"] + ":  Temp " + weatherData[0]["Temp"] + degreeSymbol + "\
            \n\tFeels " + weatherData[0]["FeelsTemp"] + degreeSymbol + "\n\tPrecip " + weatherData[0]["PrecipChance"] + "%\n"
        hour2 = weatherData[1]["Time"] + ":  Temp " + weatherData[1]["Temp"] + degreeSymbol + "\
            \n\tFeels " + weatherData[1]["FeelsTemp"] + degreeSymbol + "\n\tPrecip " + weatherData[1]["PrecipChance"] + "%\n"
        hour3 = weatherData[2]["Time"] + ":  Temp " + weatherData[2]["Temp"] + degreeSymbol + "\
            \n\tFeels " + weatherData[2]["FeelsTemp"] + degreeSymbol + "\n\tPrecip " + weatherData[2]["PrecipChance"] + "%\n"
        hour4 = weatherData[3]["Time"] + ":  Temp " + weatherData[3]["Temp"] + degreeSymbol + "\
            \n\tFeels " + weatherData[3]["FeelsTemp"] + degreeSymbol + "\n\tPrecip " + weatherData[3]["PrecipChance"] + "%\n"
        hour5 = weatherData[4]["Time"] + ":  Temp " + weatherData[4]["Temp"] + degreeSymbol + "\
            \n\tFeels " + weatherData[4]["FeelsTemp"] + degreeSymbol + "\n\tPrecip " + weatherData[4]["PrecipChance"] + "%\n"
        
        retVal = hour1 + hour2 + hour3 + hour4 + hour5
        return retVal

    def createLabel(self, root):
        global weatherLabel
        weatherLabel = tkinter.Label(root, bg="black", fg="white", font=("Arial", 25))
        weatherLabel.place(relx=1, rely=0, anchor=NE)
        weatherLabel.after(0, self.createUI)

    def createUI(self):
        global counter
        currentMinutesAndSeconds = DateAndTime.getMinutesAndSeconds()
        if (currentMinutesAndSeconds == "00:00" and counter == 0) or not locationSet:
            weatherLabel.configure(text=Weather.formattedWweatherString())
            counter += 1
        if currentMinutesAndSeconds == "00:05":
            counter = 0
        weatherLabel.after(1000, self.createUI)

