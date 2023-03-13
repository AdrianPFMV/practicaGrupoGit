def mostrar_menu():
    print("---- MENÚ ----")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")

    opcion = input("Ingrese una opción: ")

    while opcion != "5":
        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La suma de {num1} y {num2} es: {num1+num2}")
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La resta de {num1} y {num2} es: {num1-num2}")
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print(f"La multiplicación de {num1} y {num2} es: {num1*num2}")
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            if num2 != 0:
                print(f"La división de {num1} y {num2} es: {num1/num2}")
            else:
                print("No se puede dividir por cero.")
        else:
            print("Opción inválida.")
        
        opcion = input("Ingrese una opción: ")
    
    print("Programa finalizado.")
    return