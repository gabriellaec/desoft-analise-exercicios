def classifica_triangulo(a, b, c):
    if a==b and b==c:
        return 'equilátero'
    elif a!=b and a!=c and c!=b:
        return 'escaleno'
    else:
        return 'isósceles'
print(classifica_triangulo(1, 1, 1))    
        
        
  