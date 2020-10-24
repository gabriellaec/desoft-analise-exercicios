def classifica_triangulo(a,b,c):
    if a!=b and b!=c and a!=c:
        return "Escaleno"
    elif a==b and b==c and a==c:
        return "Equilatero"
    else:
        return "Isoceles"