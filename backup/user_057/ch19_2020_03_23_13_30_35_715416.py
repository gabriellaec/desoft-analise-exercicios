def classifica_triangulo (x,y,z):
    if x==y==z:
        return "equilatero"
    if x==y!=z or x==z!=y or y==z!=x:
        return "isósceles"
    else:
        return "escaleno"

print (classifica_triangulo)
