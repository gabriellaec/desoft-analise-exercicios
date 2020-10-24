def classifica_triangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        resultado = 'Triângulo Equilátero!'
    elif l1 == l2 and l2 != l3:
        resultado = 'Triângulo Isósceles!'
    else:
        resultado = 'Triângulo Escaleno!'
    return resultado