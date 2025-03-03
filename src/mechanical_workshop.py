BIENVENIDA = """
Bienvenido al taller de Don Jose.
Este programa gestiona el inventario de carros.
"""

INVENTARIO = "Este es el inventario de carros inicial:"
ACCIONES = """
Acciones:
1) Agregar carro
2) Eliminar carro
3) Ordenar inventario
4) Salir
"""

INGRESA_CARRO_AGREGAR = """
Ingresa el nombre del carro que deseas agregar:"""
INGRESA_CARRO_ELIMINAR = """
Ingresa el nombre del carro que deseas eliminar:"""
ACTUALIZACION_EXITOSA = """
Inventario actualizado:"""
ENTRADA_INVALIDA = """
Entrada invalida."""
DESPEDIDA = """
Gracias por usar este programa.
Este programa fue pythonizado por ChuyPeñaCP.
Adios."""

# Inventario inicial
carros = ["nissan", "toyota", "honda", "volkswagen", "chevrolet", "ford"]

print(BIENVENIDA)
print(INVENTARIO)

for carro in carros:
    print(carro.title())

while True:
    print(ACCIONES)
    opc = input("Dime que opcion deseas realizar: ").strip()
    
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
                    print("El carro no se encuentra en el inventario.")
                    break
            else:
                print(ENTRADA_INVALIDA)
    elif opc == "3":
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