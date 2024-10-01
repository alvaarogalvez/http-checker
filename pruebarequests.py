import requests

def iterar_archivo(path):
    try:
        with open(path, "r") as archivo:
            for linea in archivo:
                print(linea, end="")
    except FileNotFoundError:
        print("Ese archivo no existe")
    except Exception as error:
        print("[Error] " + error)

def check_status(url):
    url = add_http(url)
    try:
        respuesta = requests.get(url)
        print(respuesta.status_code, url)
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}")

def add_http(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
        return url
    else:
        return url


check = check_status("google.com")