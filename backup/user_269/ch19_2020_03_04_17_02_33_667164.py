def classifica_triangulo(a,b,c):
    if a==b or a==c or b==c:
        return("isósceles")
    elif a==b==c:
        return("equilátero")
    else:
        return("escaleno")