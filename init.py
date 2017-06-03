import requests
from bs4 import BeautifulSoup

page = requests.get("http://limbero.org/jl8/1").content
soup = BeautifulSoup(page, "html.parser")
comicImageBlock = soup.img
comicURL = comicImageBlock["src"]