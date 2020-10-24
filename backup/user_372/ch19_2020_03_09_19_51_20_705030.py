def classifica_triangulo(x, y, z):
    if x==y and y==z:
        return 'equilatero'
    elif x==y and x!=z or x==z and x!=y or y==z and z!=x:
        return 'isósceles'
    else:
        return 'escaleno'
print(classifica_triangulo(5, 5, 5).format(x, y, z))
print(classifica_triangulo(5, 5, 7).format(x, y, z))
print(classifica_triangulo(3, 4, 5).format(x, y, z))
             
    
    