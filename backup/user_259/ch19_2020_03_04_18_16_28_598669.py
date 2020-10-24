def classifica_triangulo(a,b,c):
    if a==b and a==c:
        return "equilátero"
    if a==b or a==c or b==c:
        return "isósceles"
    if a!=b and a!=c and b!=c:
        return "escaleno"
   

    
    
