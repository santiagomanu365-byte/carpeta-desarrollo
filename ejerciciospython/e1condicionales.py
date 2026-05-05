edad = int(input("Ingresá tu edad: "))

if edad < 18:
    print("Sos menor de edad")
elif 18 <= edad <= 64:
    print("Sos adulto")
else:
    print("Sos adulto mayor")