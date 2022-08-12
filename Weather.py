import requests

class Weather:
    def __init__(self, master, root):
        self.master = master
        print(self.getLocation())
        # self.getWeather()
        # self.createLabel(root)
     
     # Returns the current computers IP Address
    def getIP():
        response = requests.get("https://api64.ipify.org?format=json").json()
        return response["ip"]

    # Returns a map containing the computers IP Address, city, region name, region code, zip code, country name, and country code
    def getLocation():
        ip = Weather.getIP()
        response = requests.get(f"http://api.ipapi.com/{ip}?access_key=44ebfd0f3ed8b99deac20e713a8cc4da&format=1").json()
        location = {
            "ip": ip,
            "city": response.get("city"),
            "region_name":response.get("region_name"),
            "region_code": response.get("region_code"),
            "zip": response.get("zip"),
            "country_name": response.get("country_name"),
            "country_code": response.get("country_code")
        }
        print(location)
        return location

    # TODO
    # Try use the geocoder to get me the hourly weather for my location
    # Create a web scraper in order to get the weather data
    # Put the weather data onto the screen
