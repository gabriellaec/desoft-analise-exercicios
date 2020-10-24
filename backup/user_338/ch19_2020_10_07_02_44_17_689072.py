def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'equilatero'
    if a==b!=c:
        return 'isoceles'
    if a!=b!=c:
        return 'escaleno'
    
c=classifica_triangulo(5,5,5)
print(c)