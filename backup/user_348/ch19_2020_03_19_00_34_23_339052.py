def classifica_triangulo (a, b,c):
    if a!=b and a!=c and b!=c:
        print('escaleno')
    else: 
        if a==b or a==c or b==c: 
            print('isóceles')
        else: 
            print('equilátero')
    