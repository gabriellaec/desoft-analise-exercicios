def classifica_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_1 == lado_3 and lado_2 == lado_3:
        return 'equilatero'
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        return 'isosceles'
    else:
        return 'escaleno'
