def classifica_triangulo(a,b,c):
        if a == b:
            if b == c:
                resultado = 'equilatero'
            elif b != c:
                resultado = 'isoceles'
            else:
                resultado = 'escaleno'
        else:
            a != b
            if b == c:
                resultado = 'isoceles' 
            elif b != c:
                resultado = 'escaleno'
        return resultado
            
print(classifica_triangulo(2,2,2))
print(classifica_triangulo(2,2,3))
print(classifica_triangulo(1,2,3))
