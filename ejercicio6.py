import requests

# URL del API pública
url = "https://jsonplaceholder.typicode.com/users"

def obtener_nombres_usuarios(url):
    try:
        # Realizar la petición GET a la API
        respuesta = requests.get(url)

        # Comprobar que la petición fue exitosa
        if respuesta.status_code == 200:
            # Convertir la respuesta en formato JSON
            usuarios = respuesta.json()

            # Extraer los nombres de los usuarios
            nombres = [usuario['name'] for usuario in usuarios]
            
            return nombres
        else:
            print(f"Error en la petición: {respuesta.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Se produjo un error: {e}")
        return []

def guardar_nombres_en_archivo(nombres, archivo):
    try:
        with open(archivo, 'w') as f:
            for nombre in nombres:
                f.write(f"{nombre}\n")
        print(f"Nombres guardados en {archivo}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

if __name__ == "__main__":
    nombres_usuarios = obtener_nombres_usuarios(url)
    
    # Mostrar los nombres en pantalla
    if nombres_usuarios:
        print("Nombres de usuarios:")
        for nombre in nombres_usuarios:
            print(nombre)

        # Guardar los nombres en un archivo
        guardar_nombres_en_archivo(nombres_usuarios, "nombres_usuarios.txt")
