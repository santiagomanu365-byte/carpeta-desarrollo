velocidad = int(input("Ingresá la velocidad del vehículo (km/h): "))

if velocidad <= 60:
    print("Velocidad dentro del límite permitido")
elif 61 <= velocidad <= 80:
    print("Exceso leve de velocidad")
else:
    print("Exceso grave de velocidad")