def classifica_triangulo (lado1,lado2,lado3):
    if lado1 == lado2 and lado1 == lado3:
        triangulo_1 = 'equilátero'
        return triangulo_1
    elif  lado1 == lado2 and lado1 != lado3 or lado2 != lado3:
        triangulo_2 = 'isósceles'
        return triangulo_2
    else:
        triangulo_3 = 'escaleno'
        return triangulo_3
   