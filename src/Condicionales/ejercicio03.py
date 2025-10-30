
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, Introduzca un número válido: ")
        numero = input(mensaje)
    return int(numero)

def division(numero1: int, numero2: int) -> int:
    if numero2 == 0:
        print("Error, divisor = 0")
    else:
        division_numeros = numero1 / numero2
        print(f"El resultado es {division_numeros}")


def main():
    numero1 = pedir_numero("Introduzca el dividendo: ")
    numero2 = pedir_numero("Introduza el divisor: ")
    division(numero1, numero2)


if __name__ == "__main__":
    main()