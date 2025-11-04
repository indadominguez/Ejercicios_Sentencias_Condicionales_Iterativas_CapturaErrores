

def pedir_numero(msj:str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("Introduzca un numero válido.")
        numero = input(msj)
    return int(numero)

def calculo(numero: int):
    for i in range(1, numero + 1, 2):
        print(i, end=", ")

def main():
    numero = pedir_numero("Introduzca un número entero positivo: ")
    calculo(numero)


if __name__ == "__main__":
    main()