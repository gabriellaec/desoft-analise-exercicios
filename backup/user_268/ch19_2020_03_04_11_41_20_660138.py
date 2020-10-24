def classifica_triangulo(a, b, c):
    if a==b and b==c and a==c:
        print (str('esquilátero'))
    elif a==b or b==c or c==a:
        print (str('isósceles'))
    else:
        print (str('escaleno'))