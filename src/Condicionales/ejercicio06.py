
def pedir_nombre_sexo(mensaje: str) -> str:
    nombre = input(mensaje)
    return nombre


def separar_grupo(nombre: str, sexo: str):
    primera_letra = nombre[0].lower()
    sexo = sexo.lower()

    if (sexo == "f" and primera_letra < "m") or (sexo == "m" and primera_letra > "n"):
        print("Perteneces al Grupo A")
    else:
        print("Perteneces al grupo B")


def main():
    nombre = pedir_nombre_sexo("Introduzca su nombre por favor: ")
    sexo =  pedir_nombre_sexo("Introduzca su sexo por favor(M/F): ")

    separar_grupo(nombre, sexo)

if __name__ == "__main__":
    main()