def classifica_triangulo(a,b,c):
    if a==b==c:
        return("equilátero")
    elif a==c or b==c or a==b:
        return("isósceles")
    else:
        return("escaleno")
