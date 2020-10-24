def classifica_triangulo(a,b,c):
    if a == b and b == c:
        return "equilátero"
    if a == b or b == c or a == c:
        return "isósceles"
    if b!= a and b != c:
        return "escaleno" 