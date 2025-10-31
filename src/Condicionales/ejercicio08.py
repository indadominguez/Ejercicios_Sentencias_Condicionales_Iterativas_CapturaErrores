
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



def calcular(puntuacion: float):
    
    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
    else:
        return None, None
    
    dinero = puntuacion * 2400

    return nivel, dinero



def main():
    puntuacion = pedir_numero("Introduzca la puntuación del empleado: ")
    nivel, dinero = calcular(puntuacion)


    if nivel is None:
        print("Puntuación no válida")
    else:
        print(f"Nivel de rendimiento: {nivel}")
        print(f"Cantidad de dinero a recibir: {dinero:.2f}")

if __name__ == "__main__":
    main()