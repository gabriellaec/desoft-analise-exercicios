def classifica_triangulo(x,y,z):
    if x == y == z:
        print('equilátero')
    elif x == z or y == z or x ==z:
        print('isósceles')
    else:
        print('escaleno')