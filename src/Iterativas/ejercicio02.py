

def pedir_edad(mensaje: str) -> int:
    edad = input(mensaje)
    while not edad.isdigit():
        print("Introduzca un número válido")
        edad = input(mensaje)
    return int(edad)


def anos_cumplidos(edad: int):
    for i in range(1, edad + 1):
        print(f"Has cumplido {i} años.")


def main():
    numero = pedir_edad("Introduzca su edad real: ") 
    anos_cumplidos(numero)

if __name__ == "__main__":
    main()