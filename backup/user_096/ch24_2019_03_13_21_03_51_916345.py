def classifica_triangulo(a,b,c):
    if a==b and b==c and a==c:
        return "equilátero"
    elif a==b and a==c or b==a and b==c or c==a  and c==b:
        return "isósceles"
    elif a!=b and b!=c and a!=c:
        return "escaleno"