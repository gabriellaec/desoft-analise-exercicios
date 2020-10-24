def classifica_triangulo (a, b, c):
    if a==b and b==c and c==a: 
        return 'equilátero'
    elif a!=b and b!=c and c!=a:
        return 'escaleno'
    elif a==b or a==c or b==c:
        return 'isóceles'