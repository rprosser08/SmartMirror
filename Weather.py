import requests, MirrorMainFrame, re, urllib.request, json
from datetime import datetime


class Weather:
    global apiKey, locationSet, key
    locationSet = False

    def __init__(self, master, root):
        self.master = master
        # self.getWeather()
        # self.createLabel(root)
     
    def getLocation():
        return MirrorMainFrame.MainFrame.getLocationData()

    # Gets the location key from Accuweather needed to get the weather data for the location
    def getLocationKey():
        global apiKey, locationSet
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
        key = Weather.getLocationKey()
        URL = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + key + "?apikey=" + apiKey + "&language=en-us&details=true&metric=false"
        response = requests.get(URL)
        weatherData = response.json()
        fiveHourData = Weather.formatData(weatherData)
        print(fiveHourData)

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
            time = time_object.strftime("%I:%M %p")
            dataDictionary.update({"Time": time})

            # Gets the temperature from the weather data and stores it in the dictionary
            temp = weatherDataList[i]["Temperature"]["Value"]
            dataDictionary.update({"Temp": temp})

            # Gets the feels like temperature from the weather data and stores it in the dictionary
            feelsTemp = weatherDataList[i]["RealFeelTemperature"]["Value"]
            dataDictionary.update({"FeelsTemp": feelsTemp})

            # Gets the chance of percipitation from the weather data and stores it in the dictionary
            precipChance = weatherDataList[i]["PrecipitationProbability"]
            dataDictionary.update({"PrecipChance": precipChance})

            formattedData.append(dataDictionary)
        
        return formattedData

