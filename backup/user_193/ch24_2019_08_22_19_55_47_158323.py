def classifica_triangulo(a, b, c):
    if a==b and b==c:
        return str('equilátero')
    elif a==b and a!=c:
        return str('isósceles')
    elif a==c and a!=b:
        return str('isósceles')
    elif c==b and a!=c:
        return str('isósceles')
    elif a!=b and a!=c and b!=c:
        return str('escaleno')
    
print (classifica_triangulo(1, 2, 3))