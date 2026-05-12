saldo = float(input("Ingresá tu saldo: "))
retiro = float(input("Ingresá el monto a retirar: "))

if retiro <= saldo:
    saldo -= retiro
    print("Retiro exitoso")
    print("Saldo restante:", saldo)
else:
    print("Fondos insuficientes")