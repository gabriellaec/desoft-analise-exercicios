def classifica_triangulo(a,b,c):
    if a == b and b == c:
        print("equilátero")
    elif a != b and b != c:
        print("escaleno")
    else:
        print("isósceles")