def classifica_triangulo(a,b,c):
    if a==b and b==c and c==a:
        return 'equilátero'
    elif a!=b and a!=c and b!=c:
        return 'escaleno'
    else:
        return 'isósceles' 
print(classifica_triangulo(3,5,6))