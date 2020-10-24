def classifica_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3 :
        return("Triângulo Equilátero")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3 :
        return("Triângulo Escaleno")
    else:
        return("Triângulo Isósceles")