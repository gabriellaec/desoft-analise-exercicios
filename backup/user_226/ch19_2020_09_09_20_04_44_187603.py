def classifica_triangulos(a, b, c):
    if a == b == c:
        print("equilátero")
    elif a == b or a == c or b == c:
        print("isósceles")
    else:
        print("escaleno")