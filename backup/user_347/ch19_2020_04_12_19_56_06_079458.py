def classifica_triangulo(a, b, c):
    if a!=b and a!=c and b!=c:
        return "escaleno"
    elif a==b==c:
        return "equilátero"
    elif a==b or a==c or b==c:
        return "isóceles"