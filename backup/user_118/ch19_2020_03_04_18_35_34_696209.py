def classifica_triangulo(a,b,c):
    if (a==b and a==c):
        print('equilátero')
    elif (a==b and a!=c or a!=b and b==c or a==c and b!=c):
        print('isósceles')
    elif (a!=b and a!=c):
        print('escaleno')