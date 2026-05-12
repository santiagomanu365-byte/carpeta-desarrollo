cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje = float(input("Ingrese el porcentaje de propina: "))

propina = cuenta * (porcentaje / 100)
total = cuenta + propina

print("Monto de la propina: $", round(propina, 2))
print("Total a pagar: $", round(total, 2))