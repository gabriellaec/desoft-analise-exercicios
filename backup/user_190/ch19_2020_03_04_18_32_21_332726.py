def classifica_triangulo(a,b,c):
    if (a==b and a==c):
        print ('equilátero')
    elif (a==b and a!=c or a==c and a!=b):
        print ('isóceles')
    elif a!=b and a!=c:
        print ('escaleno')