def classifica_triangulo(x,y,z):
    if x==y and y==z:
        return ' Esse triangulo é equilátero'
    if x==y or y==z or x==z:
        return 'Esse triangulo é isósceles'
    else:
        return 'Esse triangulo é escaleno'