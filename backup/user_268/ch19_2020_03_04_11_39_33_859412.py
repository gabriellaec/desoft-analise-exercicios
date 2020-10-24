def classifica_triangulo(a, b, c):
    if a==b and b==c and a==c:
        print('esquilátero')
    elif a==b or b==c or c==a:
        print('isósceles')
    else:
        print('escaleno')