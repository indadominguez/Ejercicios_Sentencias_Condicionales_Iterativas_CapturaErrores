

def pedir_palabra(msj: str) -> str:
    palabra = input(msj)
    return palabra


def palabra_alreves(palabra: str):
    palabra_invertida = ""
    for i in range(len(palabra) - 1, -1, -1):
        palabra_invertida += palabra[i]
    return palabra_invertida


def main():
    palabra = pedir_palabra("Introduzca una palabra: ")
    print(palabra_alreves(palabra))


if __name__ == "__main__":
    main()