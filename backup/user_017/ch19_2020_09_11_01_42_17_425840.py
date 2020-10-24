def classifica_triangulo(a,b,c):
    if a == b == c:
        return "Equilatero"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Escaleno"
