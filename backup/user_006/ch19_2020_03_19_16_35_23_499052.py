def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return ("equilátero")
    elif x==y or y==z or z==x:
        return ("isósceles")
    else:
        return ("escaleno")

print(classifica_triangulo(2,4,3))