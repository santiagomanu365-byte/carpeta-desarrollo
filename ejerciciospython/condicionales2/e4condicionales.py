ingresos = float(input("Ingrese sus ingresos totales: $"))

comida = float(input("Gasto en comida: $"))
transporte = float(input("Gasto en transporte: $"))
entretenimiento = float(input("Gasto en entretenimiento: $"))

gastos_totales = comida + transporte + entretenimiento
saldo = ingresos - gastos_totales

print("\n--- Resumen del presupuesto ---")
print("Gastos totales: $", gastos_totales)
print("Saldo disponible: $", saldo)

print("\nPorcentaje de gastos:")
print("Comida:", round((comida / ingresos) * 100, 2), "%")
print("Transporte:", round((transporte / ingresos) * 100, 2), "%")
print("Entretenimiento:", round((entretenimiento / ingresos) * 100, 2), "%")