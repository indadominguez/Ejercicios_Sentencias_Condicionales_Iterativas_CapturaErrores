
def pedir_anios(mensaje: str) -> int:
    anio = input(mensaje)
    while not anio.isdigit():
        print("Introduzca un número válido")
        anio = input(mensaje)
    return int(anio)


def calcular_capital(cantidad, intereses, anios):
    capital = cantidad
    for anio in range(1, anios +1):
        capital *= 1 + intereses / 100
        print(f"Año {anio}: {capital:.2f} €") 


def main():
    cantidad = float(input("Introduce la cantidad a invertir: "))
    interes = float(input("Introduce el interés anual (en %): "))
    anios = pedir_anios("Introduce el número de años: ")
    calcular_capital(cantidad, interes, anios)


if __name__ == "__main__":
    main()