def classifica_triangulo(x, y, z):
    if x=y=z:
        return 'equilatero'
    elif: x=y!=z or x=z!=y or y=z!=x:
        return 'isósceles'
    else: x!=y!=z
        return 'escaleno'
print(classifica_triangulo(5, 5, 5))
print(classifica_triangulo(5, 5, 7))
print(classifica_triangulo(3, 4, 5))
             
    
    