def classifica_triangulo(a,b,c):
    if a == b and b == c and c == a:
        return "equilátero"
    elif a == b and c != a or a == c and b != a or c == b and a != c:
        return "isósceles"
    else:
        return "escaleno"
      