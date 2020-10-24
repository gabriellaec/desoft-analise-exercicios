def classifica_triangulo(a,b,c):
    if a!=b and c!=b and c!=a:
        return 'escaleno'
    if a!=b or a!=c or c!=b:
        return 'isósceles'
    else:
        return 'equilátero'