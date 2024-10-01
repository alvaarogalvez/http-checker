import requests

from bs4 import BeautifulSoup

url = "https://google.com"
respuesta = requests.get(url)

soup = BeautifulSoup(respuesta.text, "html.parser")   

links = [a['href'] for a in soup.find_all("a")]

for link in links:
    print(link)
