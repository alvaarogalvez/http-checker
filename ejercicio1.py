""""
print("conversor")

cadena=input("introduzca su cadena ARN para convertirla a ADN ")

def conversor(cadena):
    convertido=cadena.replace('U','T')
    return convertido

print(conversor(cadena))

"""
#ESTE SERIA EL METODO FACIL

arn="AUGC"
print(arn.replace('U','T'))


