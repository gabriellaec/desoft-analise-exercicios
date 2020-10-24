def classifica_triangulo (a,b,c):
    if a==b==c:
        return("equilátero")
    elif a==b or b==c or a==c:
        return("isóceles")
    else:
        return("escaleno")
a = 1
b = 1
c = 2