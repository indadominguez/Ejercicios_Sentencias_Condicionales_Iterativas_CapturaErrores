
def pedir_numero(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, Introduzca una edad válida")
        numero = input(mensaje)
    return int(numero)

def calcular_edad(edad: int) -> int:
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted no es mayor de edad.")


def main():
    edad = pedir_numero("Por favor, Introduzca su edad: ")
    calcular_edad(edad)


if __name__ == "__main__":
    main()