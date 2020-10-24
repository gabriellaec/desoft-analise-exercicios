def classifica_triangulo(a,b,c):
    if a==b==c:
        return("equilátero")
    if a==b and a!=c or a==c and b!=a or b==c and b!=a:
        return( "isósceles")
    if a!=b and b!=c and a!=c:
        return("escaleno")