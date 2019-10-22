"""
This script basically scrapes the gaana.com bollywood top 50 songs playlist
and provide all song names to the screen.
Just change the url in the response object with your favourite gaana.com
playlist and you are good to go.
"""
from bs4 import BeautifulSoup
import requests

res = requests.get('https://gaana.com/playlist/gaana-dj-punjabi-top-50-1')
soup = BeautifulSoup(res.text, 'lxml')
data = soup.find_all('div', {'class':'playlist_thumb_det'})

for count,i in enumerate(data, 1):
	print(count, i.text)