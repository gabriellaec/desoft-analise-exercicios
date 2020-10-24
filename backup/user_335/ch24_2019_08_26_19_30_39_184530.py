def classifica_triangulo (a,b,c):
    if (a==b and a==c):
        return ("equilátero")
    elif ((a==b and a!=c) or (a!=b and a==c) or  (b!=a and b==c)):
        return ("isóceles")
    else:
        return ("escaleno")
