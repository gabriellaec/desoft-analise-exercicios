def classifica_triangulo(x,y,z):
    if x == y and y == z and x == z:
        print('equilátero')
    elif x == z or y == z or x ==z:
        print('isósceles')
    else:
        print('escaleno')