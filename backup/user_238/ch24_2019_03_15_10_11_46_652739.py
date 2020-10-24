def classifica_triangulo(a,b,c):
    if a == b and b == c and a ==c:
        resultado = 'equilatero'
    elif (a == b and b != c) or (a != b and b == c) or (a == c and a != b):
        resultado = 'isoceles'
    elif a != b and b!=c and c !=a:
        resultado = 'escaleno'
    return resultado
        
print (classifica_triangulo(1,1,1))
print (classifica_triangulo(1,2,1))
print (classifica_triangulo(1,1,2))
print (classifica_triangulo(1,2,3))
