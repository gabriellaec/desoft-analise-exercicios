def classifica_triangulo(a,b,c):
    if a == b == c:
        print("Equilatero")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Escaleno")
