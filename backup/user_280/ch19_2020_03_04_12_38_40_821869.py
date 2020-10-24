def classifica_triangulo(a, b, c):
    if a==b and b==c:
        resultado = "equilátero"
    elif a!=b and a!=c and b!=c:
        resultado = "escaleno"
    else:
        resultado = "isósceles"
    return resultado