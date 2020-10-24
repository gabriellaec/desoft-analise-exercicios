def classifica_triangulo(a,b,c):
    if a==b==c:
        return ("equilátero")
    elif a==b!=c or b==c!=a or c==a!=b:
        return ("isóceles")
    else:
        if a!=c!=b:
        return ("escaleno")