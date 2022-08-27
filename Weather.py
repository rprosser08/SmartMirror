import requests, MirrorMainFrame, re, urllib.request, json


class Weather:
    global apiKey, locationSet, key
    # Fill in your own api key from accuweather 
    apiKey = ""
    locationSet = False

    def __init__(self, master, root):
        self.master = master
        # self.getWeather()
        # self.createLabel(root)
     
    def getLocation():
        return MirrorMainFrame.MainFrame.getLocationData()

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

    def getHourlyWeather():
        global apiKey, key, locationSet
        key = Weather.getLocationKey()
        URL = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + key + "?apikey=" + apiKey + "&language=en-us&details=true&metric=false"
        response = requests.get(URL)
        json = response.json()
        print(json)
