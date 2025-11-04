
def pedir_palabra(mensaje: str) -> str:
    palabra = input(mensaje)
    return palabra


def calcular(palabra: str):
    for i in range(1, 11):
        print(f"{i}.{palabra}")


def main():
    palabra = pedir_palabra("Introduzca una palabra: ")
    calcular(palabra)


if __name__ == "__main__":
    main()