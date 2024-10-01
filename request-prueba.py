import requests

url = "https://google.com"

respuesta = requests.get(url)

#print(respuesta.cookies)
#print(respuesta.headers)
#print(respuesta.content)
#print(respuesta.text)

def url_extractor(text):
    urls = []
    for word in text.split():
        if 'http' in word:
            urls.append(word)
    return urls

print(url_extractor(respuesta.text))