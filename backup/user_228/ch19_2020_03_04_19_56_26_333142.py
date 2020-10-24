def classifica_triangulo(a,b,c):
    if a==b==c:
        return "equilátero"
    elif a==b or a==c or c==b:
        return "isóceles"
    else:
        return "escaleno"