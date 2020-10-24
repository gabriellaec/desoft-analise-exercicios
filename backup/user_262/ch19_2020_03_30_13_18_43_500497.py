def classifica_triangulo(a,b,c):
    if a==b==c:
        return ("equilátero")
    else:
        if a==b!=c or a!=b==c or a==c!=b:
            return ("isósceles")
        else:
            return ("escaleno")