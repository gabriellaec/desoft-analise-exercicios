def classifica_triangulo(a, b, c):
    if a==b and b==c and c==a:
        return 'equilatero'
    elif a!=b and a!=c:
        return 'escaleno'
    else:
        return 'isosceles'
print(classifica_triangulo(a, b, c))    
        
        
  