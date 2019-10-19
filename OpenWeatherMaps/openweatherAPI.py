"""
Just change the appid with your API key from openweathermap API and 
you are good to go.
"""
import requests
from colorama import Fore, Style
while True:
	print("===========================")
	city = input(f"{Fore.BLUE}Enter the name of the city: {Style.RESET_ALL}")
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f34187ca28fb365a65af5ce851b14634&units=metric'.format(city)
	res = requests.get(url)
	data = res.json()
	temp = data['main']['temp']
	wind_speed = data['wind']['speed']
	lat = data['coord']['lat']
	lon = data['coord']['lon']
	description = data['weather'][0]['description']

	print("Temperature is: {} degree Celcius".format(temp))
	print("Wind Speed is: {} m/s".format(wind_speed))
	print("Latitude: {} ".format(lat))
	print("Longitude: {} ".format(lon))
	print("Description of the weather: {} ".format(description))
	if input(f'{Fore.GREEN}Do you want to repeat (y/n):{Style.RESET_ALL} ') == 'n': 
		break


