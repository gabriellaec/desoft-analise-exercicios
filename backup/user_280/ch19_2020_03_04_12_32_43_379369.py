def testa_triangulo(a, b, c):
    if a==b and b==c:
        resultado = Equilatero
    elif a==b and a!=c:
        resultado = Isosceles
    else:
        resultado = Escaleno
    return resultado

print(testa_triangulo(2, 2, 2)) 