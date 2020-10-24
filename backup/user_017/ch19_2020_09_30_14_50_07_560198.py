def classifica_triangulo(a,b,c):
    if a == b and b==c:
        return "Equilátero"
    elif a == b or a==c:
        return "Isoceles"
    else:
        return "Escaleno"
