def Mostrar_Menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
#Este es el menu y se puede llamar cuando quieras gracias a la funcion def y funciona parecido a un switch

def Opcion_Saludar() -> None:
    Nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {Nombre}! Bienvenido/a.")
#Este es la opcion saludar o sea la opcion 1 de la anterior funcion (mismo funcionamiento que un switch) y dice Hola


def Opcion_Suma() -> None:
    try:
        A = float(input("Primer número: "))
        B = float(input("Segundo número: "))
        print(f"La suma es: {A + B}")
    except ValueError:
        print(" Debes introducir valores numéricos.")
#Esta es la segunda opcion y es una suma, igualmente es una funcion y la opcion 2 del menu principal


def Opcion_Tabla() -> None:
    Numero = 5
    print(f"\nTabla del {Numero}:")
    for I in range(1, 11):
        print(f"{Numero} × {i} = {Numero * i}")
#Esta es la tercera opcion y pone la tabla de mulñtiplicar del 5 


# ---------- Bucle principal ----------
Continuar = True              
while Continuar:
#El continuar sirve como falso y verdadero ahora es verdadero y sera verdadero mientras en el menu de la funcion primera no pongas 0
    Mostrar_Menu()             
    Eleccion = input("Elige una opción: ").strip()

    if Eleccion == "1":
        opcion_saludar()
    elif Eleccion == "2":
        opcion_suma()
    elif Eleccion == "3":
        opcion_tabla()
    elif Eleccion == "0":
        print("\n ¡Hasta luego!")
        continuar = False
    else:
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")