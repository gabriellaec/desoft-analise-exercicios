def classifica_triangulo(a, b, c):
    if a==b and b==c:
        resultado = equilátero
    elif a==b and a!=c:
        resultado = isósceles
    else:
        resultado = escaleno
    return resultado

print(classifica_triangulo(2, 2, 2)) 