def classifica_triangulo (a, b,c):
    if a!=b and a!=c and b!=c:
        print('escaleno')
    else: 
        if a==b and a==c and b==c: 
        print('equilátero')
    else: 
        print('isóceles')
    