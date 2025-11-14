

def pedir_numero(msj: str) -> int:
    numero = input(msj)
    while not numero.isdigit():
        print("***ERRORRRR***, introduce un número valido.")
        numero = input(msj)
    return int(numero)

def suma_numero(numero: int) -> int:
    suma = 0

    while numero > 0:
        suma += numero % 10   
        numero //= 10  

    return suma

def main():
    numero = pedir_numero("Introduce un número válido: ")
    resultado = suma_numero(numero)
    print(f"La suma de los dígitos es {resultado}")



if __name__ == "__main__":
    main()