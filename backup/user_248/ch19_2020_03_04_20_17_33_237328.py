def classifica_triangulo(x,y,z):
    if x==y and y==z:
        return"equilátero"
    elif x!=y!=z:
        return"escaleno"
    else:
        return"isósceles"
    print(classifica_triangulo(1,1,1))