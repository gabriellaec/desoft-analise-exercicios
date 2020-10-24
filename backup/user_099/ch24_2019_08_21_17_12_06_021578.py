def classifica_triangulo(a,b,c):
    if a==b and b==c:
        return("Equilátero")
    elif a==b or b==c or a==c:
        return("Isósceles")
    else:
        return("Escaleno")
