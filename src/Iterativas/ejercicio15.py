
def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("Introduzca un valor válido.")
        numero = input(msj)
    return int(numero)

def suma_numero():
    suma = 0
    numero = pedir_numero("Introduzca un número entero: ")

    while numero != 0:
        suma += numero
        numero = pedir_numero("Introduzca un número entero: ")
    return suma


def main():
    resultado = suma_numero()
    print(f"La suma de los numeros es: {resultado}")


if __name__ == "__main__":
    main()