def classifica_triangulo(lado_1,lado_2,lado_3):
    if lado_1 == lado_2 and lado_2 == lado_3 and lado_1 == lado_3:
        resultado = "equilátero"
    elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
        resultado = "escaleno"
    else:
        resultado = "isóceles"
    return resultado