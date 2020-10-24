def classifica_triangulo(a,b,c):
    if a==b:
        if b==c:
            print('equilátero')
        else:
            print('isósceles')
    elif b==c:
        print('isósceles')
    else:
        print('escaleno')