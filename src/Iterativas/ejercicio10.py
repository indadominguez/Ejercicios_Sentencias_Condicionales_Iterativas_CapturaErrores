

def pedir_numero(msj: str) -> str:
    numero = input(msj)
    while not numero.isdigit():
        print("Introduzca un valor válido.")
        numero = input(msj)
    return int(numero)

def primo(numero: int):
    if numero < 2:
        print("No es primo")
    else:
        divisor = 2
        es_primo = True

        while divisor < numero:
            if numero % divisor == 0:
                es_primo = False
            divisor += 1

    if es_primo:
        print(" El número es primo")
    else:
        print("El número no es primo")


def main():
    numero = pedir_numero("Introduzca un número: ")
    primo(numero)


if __name__ == "__main__":
    main()