
def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("**ERROR**, Introduce un valor válido.")
        numero = input(msj)
    return int(numero)

def lista_numeros():
    suma = 0
    numero = pedir_numero("Introduce un número entero: ")
    while numero != 0:
        suma += numero
        numero = pedir_numero("Introduce un número entero: ")
    return suma


def main():
    resultado = lista_numeros()
    print(f"La sumatoria de los números ingresados es: {resultado}")

if __name__ == "__main__":
    main()