def classifica_triangulo (x, y, z):
    if x==y and x==z:
        return "Equilatero"
    elif x==y or x==z or y==z:
        return "Isosceles"
    else:
        return "escaleno"