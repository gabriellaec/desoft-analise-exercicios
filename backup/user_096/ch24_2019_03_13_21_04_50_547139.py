def classifica_triangulo(a,b,c):
    if a==b and b==c and a==c:
        return "equilátero"
    elif a==b and a==c and b!=c or b==a and b==c and a!=c or c==a  and c==b and b!=a:
        return "isósceles"
    elif a!=b and b!=c and a!=c:
        return "escaleno"