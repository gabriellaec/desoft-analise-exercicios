def classifica_triangulo(a,b,c):
    if a == b and b == c:
        resultado = 'equilatero'
    elif (a == b and b != c) or (a != b and b == c) or (a == c and a != b):
        resultado = 'isoceles'
    else:
        resultado = 'escaleno'
    return resultado
        
print (classifica_triangulo(1,1,1))
print (classifica_triangulo(1,2,1))
print (classifica_triangulo(1,1,2))
print (classifica_triangulo(1,2,3))
