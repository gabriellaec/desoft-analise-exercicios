def classifica_triangulo(x,y,z):
    if x == y and y == z and x == z:
        print('equilátero')
    elif x != y and y != z and x!= z:
        print('escaleno')
    else:
        print('isosceles')