def classifica_triangulo(a,b,c):
    if a==b and b==c:
        return "equilatero"
    elif a!=b and b!=c and a!=c:
        return "escaleno"
    else:
        return "isosceles"