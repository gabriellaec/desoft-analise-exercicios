def classifica_triangulo(a,b,c):
    if(a==b and a==c):
        return equilátero
    if(a==b and a!=c):
        return isósceles
    if(a!=b and a!=c):
        return escaleno