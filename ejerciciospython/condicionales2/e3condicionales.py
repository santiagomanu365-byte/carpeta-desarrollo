tareas = []

while True:
    print("\n--- Organizador de tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Cambiar estado")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese la tarea: ")
        tareas.append({"nombre": nombre, "estado": "Pendiente"})

    elif opcion == "2":
        for i, tarea in enumerate(tareas):
            print(i, "-", tarea["nombre"], "[", tarea["estado"], "]")

    elif opcion == "3":
        indice = int(input("Número de tarea: "))
        nuevo_estado = input("Nuevo estado (Pendiente/En progreso/Completada): ")
        tareas[indice]["estado"] = nuevo_estado

    elif opcion == "4":
        indice = int(input("Número de tarea a eliminar: "))
        tareas.pop(indice)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")