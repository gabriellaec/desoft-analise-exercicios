def classifica_triangulo(a,b,c):
    if a==b==c:
        return ("equilátero")
    else:
        if a==b!=c:
        return ("isóceles")
    else:
        if a!=c!=b:
            return ("escaleno")