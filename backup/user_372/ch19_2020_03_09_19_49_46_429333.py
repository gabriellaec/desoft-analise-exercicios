def classifica_triangulo(x, y, z):
    if x==y and y==z:
        return 'equilatero'
    elif x==y and x!=z or x==z and x!=y or y==z and z!=x:
        return 'isósceles'
    else x!=y and x!=z and y!=z:
        return 'escaleno'
print(classifica_triangulo(5, 5, 5))
print(classifica_triangulo(5, 5, 7))
print(classifica_triangulo(3, 4, 5))
             
    
    