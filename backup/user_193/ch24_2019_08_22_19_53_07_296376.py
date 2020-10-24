def classifica_triangulo(a, b, c):
    if a==b and b==c:
        return str('equilátero')
    elif a==b or a==c or b==c and a!=c or a!=b or a!=b:
        return str('isósceles')
    elif a!=b and a!=c and b!=c:
        return str('escaleno')
    
print (classifica_triangulo(5, 5, 5))