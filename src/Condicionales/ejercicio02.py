
def pedir_contraseña(mensaje: str) -> str:
    contraseña = input(mensaje)
    return contraseña


def calcular_contraseña(contraseña_introducida: str):

    contraseña = "Bocadillo"

    if contraseña_introducida.lower() == contraseña.lower():
        print("La contraseña es correcta")
    else:
        print("Vuelva a intertarlo por favor")
    

def main():
    contraseña_introducida = pedir_contraseña("Introduzca la contraseña: ")
    calcular_contraseña(contraseña_introducida)

if __name__ == "__main__":
    main()