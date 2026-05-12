print("Conversor de unidades")
print("1. Kilómetros a millas")
print("2. Celsius a Fahrenheit")

opcion = int(input("Elija una opción: "))

if opcion == 1:
    km = float(input("Ingrese kilómetros: "))
    millas = km * 0.621371
    print("Equivale a", round(millas, 2), "millas")

elif opcion == 2:
    celsius = float(input("Ingrese grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Equivale a", round(fahrenheit, 2), "grados Fahrenheit")

else:
    print("Opción inválida")