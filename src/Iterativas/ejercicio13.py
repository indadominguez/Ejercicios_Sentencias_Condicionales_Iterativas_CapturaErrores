

def pedir_frase(msj: str) -> str:
    frase = input(msj)
    return frase

def eco():
    entrada = pedir_frase("Introduzca una frase(o 'salir' para continuar): ")
    while entrada != "salir":
        print("Eco:", entrada)
        entrada = pedir_frase("Introduzca una frase(o 'salir' para continuar): ")
    return  "Programa Terminado"


def main():
    resultado = eco()
    print(resultado)

if __name__ == "__main__":
    main()