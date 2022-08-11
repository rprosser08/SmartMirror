import geocoder

class Weather:
    def __init__(self, master, root):
        self.master = master
        self.getLocation()
        # self.getWeather()
        # self.createLabel(root)
        # self.createUI()

    # will return the location of the current user
    def getLocation():
        g = geocoder.ip("me")
        print(g.latlng)
        print(g.city)

    # TODO
    # Try use the geocoder to get me the hourly weather for my location
    # Create a web scraper in order to get the weather data
    # Put the weather data onto the screen
