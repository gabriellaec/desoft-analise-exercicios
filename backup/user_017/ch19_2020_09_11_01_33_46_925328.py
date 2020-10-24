def classifica_triangulo(a,b,c):
    if a == b == c:
        print("Equilatero")
    elif a == b and a != c:
        print("Isosceles")
    else:
        print("Escaleno")
