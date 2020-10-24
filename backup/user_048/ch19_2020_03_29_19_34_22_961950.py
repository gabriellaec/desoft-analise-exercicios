def classifica_triangulo(x,y,z):
    if x==y==z:
        print("equilátero")
    elif x==y!=z or x==z!=y or y==z!=x:
        print("isósceles")
    else:
        print("escaleno")