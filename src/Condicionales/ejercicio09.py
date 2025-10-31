

def pedir_edad(mensaje: str) -> int:
    numero = input(mensaje)
    while not numero.isdigit() or not (1 <= int(numero) < 100):
        print("Por favor, Introudzca un valor válido")
        numero = input(mensaje)
    return int(numero)
    


def calculo_entrada(edad: int):
    if edad < 4:
        entrada = "Puede entrar gratis"
    elif 4 <= edad <= 18:
        entrada = "Debe pagar 5€"
    else:
        entrada = "Debe pagar 10€"
    return entrada

def main():
    edad = pedir_edad("Introduzca su edad: ")
    resultado = calculo_entrada(edad)
    print(resultado)



if __name__ == "__main__":
    main()