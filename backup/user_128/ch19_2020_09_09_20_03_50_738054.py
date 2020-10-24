def classifica_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        equilatero = "equilátero"
        return equilatero

    elif lado1 == lado2 and lado1 != lado3:
        isoceles = "isósceles"
        return isoceles

    elif lado1 == lado3 and lado1 != lado2:
        isoceles = "isósceles"
        return isoceles

    elif lado2 == lado3 and lado1 != lado2:
        isoceles = "isósceles"
        return isoceles

    else:
        escaleno = "escaleno"
        return escaleno