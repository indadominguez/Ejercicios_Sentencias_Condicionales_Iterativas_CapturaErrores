

def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("***ERRORRRR***, introduce un número valido.")
        numero = input(msj)
    return int(numero)


def mayor_numero():
    numero = pedir_numero("Introduce un número entero positivo: ")
    mayor = None

    while numero != 0:
        if mayor is None or numero > mayor:
            mayor = numero
        numero = pedir_numero("Introduce un número entero positivo: ")

    return mayor


def mostrar_mayor(mayor: int | None) -> None:
    if mayor is not None:
        print(f"El número más alto es {mayor}")
    else:
        print("No se han introducido números.")


def main():
    resultado = mayor_numero()
    mostrar_mayor(resultado)


if __name__ == "__main__":
    main()