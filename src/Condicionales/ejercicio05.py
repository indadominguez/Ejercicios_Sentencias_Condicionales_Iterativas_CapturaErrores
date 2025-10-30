
def pedir_edad(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit():
        print("Por favor, Introduzca una edad válida")
        numero = input(mensaje)
    return int(numero)

def pedir_ingresos(mensaje: str) -> float:
    correcto = False
    numero = input(mensaje)
    while not correcto:
        try:
            numero_float = float(numero)
            correcto = True
        except ValueError:
            print("Por favor, introduzca un número válido.")
            numero = input(mensaje)
    return numero_float


def calculo(edad: int, ingresos: float):
    if edad > 16 and ingresos >= 1000:
        print("El usuario puede tributar")
    else:
        print("El usuario no puede tributar") 


def main():
    edad = pedir_edad("Introduzca su edad: ")
    ingresos = pedir_ingresos("Introduzca sus ingresos: ")
    calculo(edad, ingresos)

if __name__ == "__main__":
    main()