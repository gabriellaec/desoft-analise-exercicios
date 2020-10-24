import math

def classifica_triangulo(c1, c2, c3):
    if c1 == c2 == c3:
        return "equilátero"
    if c1 != c2 and c2 != c3 and c1 != c3:
        return "escaleno"
    if (c1 == c2 and c1 != c3) or (c1 == c3 and c1 != c2) or (c2 == c3 and c2 != c1):
        return "isósceles"
    
print(classifica_triangulo(10, 10, 10))
print(classifica_triangulo(10, 10, 5))
print(classifica_triangulo(10, 15, 5))