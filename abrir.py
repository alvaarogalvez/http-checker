def iterar_archivo(path):
    try:
         with open(path, "r") as archivo:
            for linea in archivo:
                print(linea, end="")
    except FileNotFoundError:
        print("ese archivo no existe")
    except Exception as e:
        print("Error" + e)

iterar_archivo("domain")