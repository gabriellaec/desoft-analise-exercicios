def classifica_triangulo(a,b,c):
    if a == b == c:
        print("equilátero")
    if a == b or b == c or a == c:
        print("isósceles")
    else:
        print("escaleno")