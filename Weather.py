import requests, MirrorMainFrame, re, urllib.request, json
from DateAndTime import DateAndTime
from datetime import datetime
from tkinter import *
import tkinter
import PIL.Image
import PIL.ImageTk


class Weather:
    global apiKey, locationSet, key, counter, tkRoot
    locationSet = False
    counter = 0
    Location_data = ""
    Current_weather_data = {"WeatherText": "", "WeatherIcon": "0", "Temperature": "0"}

    def __init__(self, master, root):
        self.master = master
        global tkRoot
        tkRoot = root
        self.weatherLabel(root)
     
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
        Weather.Location_data = json
        key = json[0]["Key"]
        # locationSet = True
        return key

    # Returns the city, state, zip code, and country code where the weather data is from
    def get_users_location():
        location_name = Weather.Location_data[0]['LocalizedName']
        location_state = Weather.Location_data[0]['AdministrativeArea']['ID']
        location_zip = Weather.Location_data[0]['PrimaryPostalCode']
        location_country = Weather.Location_data[0]['AdministrativeArea']['CountryID']
        return location_name, location_state, location_zip, location_country


    def getCurrentWeather():
        global apiKey, key, locationSet
        Weather.setAPIKey()
        if not locationSet:
            Weather.setLocationKey()
        URL = "http://dataservice.accuweather.com/currentconditions/v1/" + key + "?apikey=" + apiKey
        response = requests.get(URL)
        weatherData = response.json()
        Weather.formatWeather(weatherData)

    # Gets the Accuweahter API key from the file "APIKey.txt"
    def setAPIKey():
        global apiKey
        with open("APIKey.txt") as f:
            apiKey = f.read()

    def formatWeather(weatherData):
        weather_text = weatherData[0]["WeatherText"]
        weather_icon = weatherData[0]["WeatherIcon"]
        temp = int(weatherData[0]["Temperature"]["Imperial"]["Value"])
        Weather.Current_weather_data["WeatherText"] = weather_text
        Weather.Current_weather_data["WeatherIcon"] = str(weather_icon)
        Weather.Current_weather_data["Temperature"] = str(temp)

    def current_weather_string():
        degreeSymbol = "\u00B0"
        Weather.getCurrentWeather()
        user_location_data = Weather.get_users_location()
        ret_val = []
        temp = Weather.Current_weather_data["Temperature"] + degreeSymbol + "F\n"
        ret_val.append(temp)
        data = user_location_data[0] + ", " + user_location_data[1] + ", " + user_location_data[3] + "\n" + Weather.Current_weather_data["WeatherText"]
        ret_val.append(data)
        return ret_val


    def weatherLabel(self, root):
        global weatherCanvas, tkRoot
        weather_strings = Weather.current_weather_string()
        temp_string = weather_strings[0]
        data_string = weather_strings[1]
        weatherCanvas = tkinter.Canvas(root, bg="black", bd=0, highlightthickness=0, relief="ridge")
        weatherCanvas.place(relx=0.9, rely=0.075, anchor=CENTER)
        weatherCanvas.after(0, self.createUI)


    def createUI(self):
        global tkRoot, counter, locationSet
        currentMinutesAndSeconds = DateAndTime.getMinutesAndSeconds()
        # Ensures the weather data is only updated once per hour
        if (currentMinutesAndSeconds == "00:00" and counter == 0) or not locationSet:
            weather_strings = Weather.current_weather_string()
            temp_string = weather_strings[0]
            data_string = weather_strings[1]

            # Prepares the correct weather icon to be displayed
            weatherIcon_file = "./weatherIcons/" + Weather.Current_weather_data["WeatherIcon"] + ".png"
            img = tkinter.PhotoImage(file=weatherIcon_file)
            tkRoot.img = img

            # Update is used to get the current dimensions of the weather canvas 
            weatherCanvas.update()
            canvas_width = weatherCanvas.winfo_width()
            canvas_height = weatherCanvas.winfo_height()

            weatherCanvas.create_image(canvas_width/3 - 20, canvas_height/3, image=img, anchor=E)
            weatherCanvas.create_text(canvas_width/3, canvas_height/3 + 15, text=temp_string, fill="white", font=("Arial", 25))
            weatherCanvas.create_text(canvas_width/2, canvas_height/2 + 15, text=data_string, fill="white", font=("Arial", 25))

            counter += 1
            locationSet = True
        else:
            counter = 0

        weatherCanvas.after(1000, self.createUI)

