def tipo_de_triangulo(a,b,c):
    if a == b and a == c:
        print('equilátero')
        return 'equilatero'
    elif a==b or a==c or b==c:
        print ('isósceles')
        return 'isósceles'
    else:
        print('escaleno')
        return 'escaleno'