def classifica_triangulo(x,y,z):
    if x and y and z == 1:
        return 'Isso nao é um triangulo'
    if x==y and y==z:
        return ' Esse triangulo é equilatero'
    if x==y or y==z or x==z:
        return 'Esse triangulo é isocele'
    else:
        return 'Esse triangulo é escaleno'