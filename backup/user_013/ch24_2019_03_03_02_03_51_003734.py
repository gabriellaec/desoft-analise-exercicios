def classifica_triangulo(a,b,c):
    if a == b and a == c:
        return "equilátero"
    elif not a!=b and a!=c and b!=c:
        return "isóceles"
    else:
        return "escaleno"
    