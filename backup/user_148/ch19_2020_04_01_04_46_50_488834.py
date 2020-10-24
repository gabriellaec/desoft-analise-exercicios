def classifica_triangulo(x, y, z):
    if x==y==z:
        print('equilátero')
    elif x!=y!=z:
        print('escaleno')
    elif x==y and y!=z or x==z and z!=y or y==z and x!=z:    
        print('isósceles')