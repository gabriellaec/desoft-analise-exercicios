def classifica_triangulo(a,b,c):
    if a == b and a == c:
        return "equilátero"
    else:
        if a == b and c != a or b == c and a != b:
            return "isóceles"
        else:
            return "escaleno"

print(classifica_triangulo(3, 3, 3))
print(classifica_triangulo(1, 1, 2))
print(classifica_triangulo(3, 4, 5))