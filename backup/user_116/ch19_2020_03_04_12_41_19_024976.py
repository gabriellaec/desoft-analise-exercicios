def classifica_triangulo.(x,y,z):
    if x == y and x == z and y == z:
        return'equilátero'
    elif x==y or x==z or y==z:
        return'isóceles'
    else:
        return'escaleno'