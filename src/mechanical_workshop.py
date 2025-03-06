BIENVENIDA = """
Bienvenido al taller de Don José.
Este programa gestiona el inventario de carros.
"""

INVENTARIO = "Este es el inventario actual de carros:"
ACCIONES = """
Acciones:
1) Agregar un carro
2) Eliminar un carro
3) Ordenar el inventario
4) Salir
"""

INGRESA_CARRO_AGREGAR = """
Ingresa el modelo del carro que deseas agregar: """
INGRESA_CARRO_ELIMINAR = """
Ingresa el modelo del carro que deseas eliminar: """
ACTUALIZACION_EXITOSA = """
Inventario actualizado:"""
ENTRADA_INVALIDA = """
Entrada inválida."""
DESPEDIDA = """
Gracias por usar este programa.
Este programa fue pythonizado por ChuyPeñaCP.
Adiós."""

# Inventario inicial
carros = ["sentra", "corolla", "civic", "jetta", "aveo", "mustang"]

# Función principal del programa
def iniciar_taller():
    print(BIENVENIDA)
    print(INVENTARIO)

    for carro in carros:
        print(carro.title())

    while True:
        print(ACCIONES)
        opc = input("Dime qué opción deseas realizar: ").strip()
        
        if opc == "1":
            # Agregar carro
            while True:
                carro = input(INGRESA_CARRO_AGREGAR).strip().lower()
                if carro != "":
                    carros.append(carro)
                    print(ACTUALIZACION_EXITOSA)
                    for carro in carros:
                        print(carro.title())
                    break
                else:
                    print(ENTRADA_INVALIDA)
        elif opc == "2":
            # Eliminar carro
            while True:
                carro = input(INGRESA_CARRO_ELIMINAR).strip().lower()
                if carro != "":
                    if carro in carros:
                        carros.remove(carro)
                        print(ACTUALIZACION_EXITOSA)
                        for carro in carros:
                            print(carro.title())
                        break
                    else:
                        print("El modelo ingresado no está en el inventario.")
                else:
                    print(ENTRADA_INVALIDA)
        elif opc == "3":
            # Ordenar inventario
            carros.sort()
            print(ACTUALIZACION_EXITOSA)
            for carro in carros:
                print(carro.title())
        elif opc == "4":
            # Salir del programa
            print(DESPEDIDA)
            break
        else:
            print(ENTRADA_INVALIDA)

# Solo ejecuta la función si este archivo es el principal
if __name__ == "__main__":
    iniciar_taller()