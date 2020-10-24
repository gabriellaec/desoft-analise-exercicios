def classifica_triangulo(a,b,c):
    if(a==b and a==c and b==c):
        return "equilátero"
    if(a!=b and a!=c and b!=c):
        return "escaleno"
    else:
        return "isósceles"