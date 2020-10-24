#classifica_triangulo
def classifica_triangulo (a,b,c):
    if a==b and a==c and b==c:
        print ('equilátero')
    if a==b or a==c or b==c:
        print ('isósceles')
    if a!=b and a!=c and b!=c:
        print ('escaleno')
    