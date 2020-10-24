def testa_tipo_de_triangulo(lado1, lado2, base):
    if lado1 == lado2 and lado1 == base and lado2 == base:
        equilátero = 'seu triânglo é equilatero'
        return equilátero
    elif (lado1 == lado2 and base != lado1) or (lado1 == base and lado1 != lado2) or (lado2 == base and lado2 != lado1):
        isósceles = 'seu triângulo é isósceles'
        return isósceles
    else: 
        escaleno = 'seu triângulo é escaleno'
        return escaleno

c = testa_tipo_de_triangulo(9, 10, 8)
print(c)