def classifica_triangulo(a,b,c):
    if a==b==c:
        return("equilátero")
    if a==b!=c or a==c!=b or b==c!=a:
        return("isósceles")
    else: 
        return("escaleno")