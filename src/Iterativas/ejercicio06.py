

def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("Introduzca un número válido.")
        numero = input(msj)
    return int(numero)


def calcular_triangulo(altura: int):
    for i in range(1, altura + 1):
        print("*" * i )


def main():

    altura = pedir_numero("Introduzca la altura del triángulo: ")
    calcular_triangulo(altura)



if __name__ == "__main__":
    main()