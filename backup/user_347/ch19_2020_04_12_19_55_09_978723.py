def classifica_triangulo(a, b, c):
    if a!=b and a!=c and b!=c:
        return "escaleno"
    elif a==b and a==c and b==c:
        return "equilátero"
    else:
        return "isóceles"