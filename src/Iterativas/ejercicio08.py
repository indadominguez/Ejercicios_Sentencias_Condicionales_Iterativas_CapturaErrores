

def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("Introduzca un número correcto.")
        numero = input(msj)
    return int(numero)

def triangulo(numero: int):
    for i in range (1, numero + 1, 2):
        j = i
        while j >= 1:
            print(j, end=" ")
            j -= 2
        print()


def main():
    numero = pedir_numero("Introduzca un número entero: ")
    triangulo(numero)



if __name__ == "__main__":
    main()