def classifica_triangulo(lado_a, lado_b, lado_c):
    if lado_a == lado_b and lado_b == lado_c and lado_a == lado_c:
        return 'equilátero'
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        return 'isósceles'
    else:
        return 'escaleno'
print(classifica_triangulo(1,1,2))

