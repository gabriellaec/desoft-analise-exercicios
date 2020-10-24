def classifica_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
        return "equilátero"
    elif lado1!=lado2 and lado3 != lado2 and lado3 != lado1:
        return "escaleno"
    else:
        return "isósceles"