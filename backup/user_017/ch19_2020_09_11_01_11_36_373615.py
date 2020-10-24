def classifica_triangulo(a,b,c):
    if a == b and a == c:
        return "Equilatero"
    elif a == b and a != c:
        return "Isosceles"
    else:
        return "Escaleno"
