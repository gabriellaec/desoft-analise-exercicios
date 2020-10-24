def classifica_triangulo(a,b,c):
    if a == b and a == c:
        print('equilátero')
        return 'equilátero'
    elif a==b or a==c or b==c:
        print ('isósceles')
        return 'isósceles'
    else:
        print('escaleno')
        return 'escaleno'