def classifica_triangulo(lados):
    if lados == 3:
        return 'equilátero'
    elif lados == 2:
        return 'isóceles'
    else:
        return 'escaleno'
print(classifica_triangulo(3))
print(classifica_triangulo(2))
print(classifica_triangulo(1))
    