


def pedir_palabra(msj: str) -> str:
    palabra = input(msj)
    return palabra


def pedir_vocal(msj: str) -> str:
    vocal = input(msj)
    return vocal


def contar_letra(palabra: str, vocal: str) -> int:
    contador = 0
    for letra in palabra:
        if letra.lower() == vocal.lower():
            contador += 1
    return contador


def main():
    palabra = pedir_palabra("Introduzca una palabra: ")
    vocal = pedir_vocal("Introduzca una vocal: ")
    total = contar_letra(palabra, vocal)
    print(f"La vocal {vocal} aparece {total} veces en la palabra {palabra}. ")



if __name__ == "__main__":
    main()