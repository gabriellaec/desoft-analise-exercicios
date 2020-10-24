def classifica_triangulo(a,b,c):
    if a==b==c :
        print('equilatero')
    elif a==b!=c or a!=b==c or a==c!=b :
        print('isosceles')
    else :
        print('escaleno')
    int(input('Digite os tres lados:',a,b,c)
        return ()