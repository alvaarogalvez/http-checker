#from abrir import iterar_archivo

#iterar_archivo("domains")

import requests
def iterar_archivo(path):
    try:
         with open(path, "r") as archivo:
            for linea in archivo:
                print(linea, end="")
    except FileNotFoundError:
        print("ese archivo no existe")
    except Exception as e:
        print("Error" + e)


def check_status(url):
    try:
        respuesta = requests.get(url)
        print(respuesta.status_code, url)
    except request.exceptions.RequestException as error:
        print(f"[Error] {error}")

def add_http(url):
    if not url.startWith("http://") and not url.startswith("https://"):
        url="https://" + url
        return url

check_status("https://google.com")
