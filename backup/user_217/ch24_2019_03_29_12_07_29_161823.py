def classifica_triangulo(a,b,c):
    if a==b==c:
        print('equilátero')
    elif a==b!=c and a!=b==c:
        print('isosceles')
    else:
        print('escaleno')
    return classifica_triangulo