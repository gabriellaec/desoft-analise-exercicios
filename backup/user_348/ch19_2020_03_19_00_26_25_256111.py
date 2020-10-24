def classifica_triangulo (a, b,c):
    if a!=b and a!=c and b!=c:
        print('escaleno')
    elif a==b and a==c and b==c: 
        print('equilátero')
    else: 
        print('isóceles')
    