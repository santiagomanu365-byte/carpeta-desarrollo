import random
import string

# Solicitar datos
longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Contraseña generada:", contraseña)