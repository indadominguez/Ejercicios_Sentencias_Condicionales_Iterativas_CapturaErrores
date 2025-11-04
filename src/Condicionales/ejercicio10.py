
def pedir_pizza():
    print("BIENVENIDO A PIZZERIA BELLA NAPOLI 🍕")
    tipo = input("Introduzca si quiere una pizza vegetariana (si/no) :").lower()
    if tipo == "sí" or tipo == "si":
        return "Vegetariana"
    else:
        return "no vegetariana"


def calcular_ingredientes(tipo):
    if tipo == "Vegetariana":
        return input("Elige un ingrediente (Pimiento o Tofu): ").lower()
    
    else:
        return input("Elige un ingrediente (Jamón, Salmón, Peperoni): ").lower()
    

def mostrar_pizza(tipo, ingrediente):
    print(f"Usted ha elegido una pizza {tipo} y lleva mozarrella, tomate y {ingrediente} ")


def main():
    pedido = pedir_pizza()
    ingrediente = calcular_ingredientes(pedido)
    mostrar_pizza(pedido, ingrediente)

if __name__ == "__main__":
    main()