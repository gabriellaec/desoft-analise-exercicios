#Tipo de triângulo
def classifica_triangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Equilatéro"

    elif lado1 != lado2 and lado2 == lado3 or lado1 == lado2 and lado2 != lado3 or lado1 == lado3 and lado1!=lado2:
        return "Isósceles"

    else:
        return "Escaleno"