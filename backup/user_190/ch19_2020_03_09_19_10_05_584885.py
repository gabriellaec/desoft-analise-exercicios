def classifica_triangulo(a,b,c):
    if (a==b and a==c):
        return ('equilátero')
    elif (a==b and a!=c or a==c and a!=b or b==c and b!=a):
        return ('isóceles')
    elif a!=b and a!=c:
        return ('escaleno')