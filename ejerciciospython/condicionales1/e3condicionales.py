print("Menú:")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Ensalada")
print("4. Salir")

opcion = int(input("Elegí una opción: "))

match opcion:
    case 1:
        print("Elegiste Hamburguesa")
    case 2:
        print("Elegiste Pizza")
    case 3:
        print("Elegiste Ensalada")
    case 4:
        print("Saliendo del programa...")
    case _:
        print("Opción inválida")