def classifica_triangulo(a,b,c):
    if a==b==c:
        return ('Equilátero')
    if a!=b==c or a==b!=c or a==c!=b:
        return ('Isósceles')
    if a!=b!=c:
        return ('Escaleno')

    