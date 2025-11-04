

def pedir_numero(msj:str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("Introduzca un numero válido.")
        numero = input(msj)
    return int(numero)

def cuenta_regresiva(numero: int):
    for i in range(numero, 0, -1):
        if i > 1:
            print(i, end=", ")
        else:
            print(f"{i}.")

def main():
    numero = pedir_numero("Introduzca un número entero positivo: ")
    cuenta_regresiva(numero)


if __name__ == "__main__":
    main()