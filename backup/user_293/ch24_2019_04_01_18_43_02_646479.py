def classifica_triangulo(a,b,c):
    if a != b and b != c:
        return "escaleno"
    elif a == b and b == c:
        return "equilátero"
    else:
        return "isósceles"
    
        