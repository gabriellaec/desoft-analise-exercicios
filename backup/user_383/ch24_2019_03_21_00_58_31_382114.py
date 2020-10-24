def classifica_triangulo(a,b,c):
    if a==b and b==c:
        print('equilátero')
    elif a==b and b!=c or a==c and b!=a or b==c and a!=c:
        print('isósceles')
    else:
        print('escaleno')