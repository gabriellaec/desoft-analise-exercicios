def classifica_triangulo(a,b,c):
    if a==b==c:
        return ("equilátero")
    else:
        if a==b!=c:
            return ("isósceles")
        else:
            return ("escaleno")