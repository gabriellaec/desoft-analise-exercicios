def classifica_triangulo(a,b,c):
    if a == b and a == c:
        return "equilátero"
    elif a == b or a == c or c == b: 
        return "isósceles"
    else: 
        return  "escaleno"