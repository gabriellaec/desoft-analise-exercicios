def classifica_triangulo(a,b,c):
    if a==b==c:
        print("equilátero")
    if a==b and a!=c or a==c and b!=a or b==c and b!=a:
        print( "isósceles")
    if a!=b and b!=c and a!=c:
        print("escaleno")