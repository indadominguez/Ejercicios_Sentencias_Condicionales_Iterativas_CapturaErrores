
def pedir_contrasena(mensaje: str) -> str:
    contrasena = input(mensaje)
    return contrasena

def contrasena_correcta():
    contrasena = "Inda1234".lower()
    contrasena_introducida = pedir_contrasena("Introduce la contraseña: ").lower()

    while not contrasena_introducida == contrasena:
        if contrasena_introducida != contrasena:
            print("Contraseña incorrecta. Inténtelo de nuevo: ")
        contrasena_introducida = pedir_contrasena("Introduce la contraseña: ").lower()

    else:
            print("Contraseña correcta")


def main():
    contrasena_correcta()


if __name__ == "__main__":
    main()