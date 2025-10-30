

def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, Introduzca un número válido")
        numero = input(mensaje)
    return int(numero)


def par_impar(numero: int):
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")


def main():
    numero = pedir_numero("Introduzca un número: ")
    par_impar(numero)


if __name__ == "__main__":
    main()