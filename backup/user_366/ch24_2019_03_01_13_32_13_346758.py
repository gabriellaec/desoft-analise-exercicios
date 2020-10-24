def classifica_triangulo(a, b, c):
    if a==b==c==a:
        return "equilátero"
    elif a!=b!=c!=a:
        return "escaleno"
    else:
        return "isósceles"