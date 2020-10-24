def classifica_triangulo(a,b,c):
    if (a==b and a==c):
        print('equilátero')
    elif (a==b or a!=b or a==c):
        print('isósceles')
    else:
        print('escaleno')