def classifica_triangulo(a, b, c):
    if a == b and a == c:
        return "equilatero"
   	elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "escaleno"