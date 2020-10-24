def classifica_triangulo(a,b,c):
    if a == b and a == c:
        return "equilátero"
    else:
        if a == b and c != a or b == c and a != b:
            return "isósceles"
        else:
            return "escaleno"

print(classifica_triangulo(1, 1, 2))