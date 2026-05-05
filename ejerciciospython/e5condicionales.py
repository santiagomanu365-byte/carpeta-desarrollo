dia = int(input("Ingresá un número del 1 al 7: "))

if 1 <= dia <= 5:
    print("Día laboral")
elif dia == 6 or dia == 7:
    print("Fin de semana")
else:
    print("Número inválido")