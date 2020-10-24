import math
def classifica_triangulo(a,b,c):
    if a == b and b == c and a == c:
        return "equilátero"
    elif a == b and a != c and b != c :
        return "isósceles"
    elif a == c and a != b and c != b:
        return "isósceles"
    elif b == c and b != a and c!= a:
        return "isósceles"
    else:         
        return "escaleno"
classifica_triangulo(1,2,4)