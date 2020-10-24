def classifica_triangulo(x, y, z):
    if x==y and y==z:
        return "equilátero"
    elif x==y or x==z or z==y:
        return "isóseles"
    else:
        return "escaleno"

    