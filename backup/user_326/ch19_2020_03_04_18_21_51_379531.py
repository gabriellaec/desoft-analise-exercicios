def classifica_triangulo(lado1, lado2, base):
    if lado1 == lado2 and lado1 == base and lado2 == base:
        equilátero = 'equilatero'
        return equilátero
    elif (lado1 == lado2 and base != lado1) or (lado1 == base and lado1 != lado2) or (lado2 == base and lado2 != lado1):
        isósceles = 'isósceles'
        return isósceles
    else: 
        escaleno = 'escaleno'
        return escaleno

c = classifica_triangulo(9, 10, 8)
print(c)