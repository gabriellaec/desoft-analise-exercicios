def classifica_triangulo(a,b,c):
    if a == b == c:
        return 'equilátero'
    elif a == b != c or a == c != b or b == c != a:
        return 'isósceles'
    else:
        return 'escaleno'
   
print(classifica_triangulo(3,3,3))
print(classifica_triangulo(3,4,5))
print(classifica_triangulo(4,4,3))