def classifica_triangulo(a,b,c):
    if a == b and b == c and c == a:
        print("equilatero")
    elif a == b and c != a or a == c and b != a or c == b and a != c:
        print("isóceles")
    else:
        print("escaleno")
      