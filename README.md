# SmartMirror

## Project Description
This code is for the GUI component of a smart mirror. It will include the current time and date, the current weather, and your calendar events for the day.

## Instructions
Once you clone this git repository you will need to set a couple of things up. Firstly, you will need to create a free account with Accuweather to use their API. Once you have recieved an API key you can enter it into the provided "APIKeyExample.txt" file, which you will want to rename to "APIKey.txt". 

Then, you will want to make sure you have all of the correct packages installed. You can do so with the following commands. <br />
<br />
sudo pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib <br />
sudo pip3 install pillow --upgrade <br />

Finally, you will run the code from the startScreen.py file and enter in your zip code on the start screen and press enter. This can be done from the terimal, by navigating to the correct folder and enterting the following command. <br />
<br />
python3 startScreen.py

## TODO
- Formatting the user screens

## References
Code for the calendar was taken and modified from https://developers.google.com/calendar/api/quickstart/python (Calendar.py -> main function) <br />
Weather Icons taken from https://developer.accuweather.com/weather-icons