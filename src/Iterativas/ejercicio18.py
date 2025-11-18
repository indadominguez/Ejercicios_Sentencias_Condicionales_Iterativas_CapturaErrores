

def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not (numero.isdigit() or numero == "-1"):
        print("Introduce un número válido")
        numero  =input(msj)
    return int(numero)


def suma_numero(numero: int) -> int:
    suma = 0

    while numero > 0:
        suma += numero % 10   
        numero //= 10  

    return suma


def calculo_numero():
    contador_pares = 0 
    numero = pedir_numero("Introduzca un número: ")


    while numero != -1:
        suma = suma_numero(numero)
        print(f"La suma de los dígitos de {numero} es {suma}")

        if numero % 2 == 0:
            contador_pares += 1

        numero = pedir_numero("Introduzca un número: ")

    print(f"Se ingresaron {contador_pares} números pares.")


def main():
    calculo_numero()


if __name__ == "__main__":
    main()