

def pedir_numero(mensaje: str) -> float :
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


def tramos_impositivos(renta_anual: float):
    if renta_anual < 10000:
        print("Le corresponde a pagar: 5%")
    elif renta_anual < 20000:
        print("Le corresponde a pagar: 15%") 
    elif renta_anual < 35000:
        print("Le corresponde a pagar: 20%")
    elif renta_anual < 60000:
        print("Le corresponde a pagar: 30%")
    else:
        print("Le corresponde a pagar: 45%")


def main():
    renta = pedir_numero("Introduzca su renta anual: ")
    tramos_impositivos(renta)



if __name__ == "__main__":
    main()