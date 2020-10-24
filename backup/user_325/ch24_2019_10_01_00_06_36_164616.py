def classifica_triangulo(a, b, c):
    if a == b and b != c:
        print("isósceles")
    elif a != b and b != c:
        print("escaleno")
    else:
        print("equilátero")
print(classifica_triangulo(a, b, c))        

    