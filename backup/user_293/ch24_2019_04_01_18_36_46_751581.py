def classifica_triangulo(a,b,c):
    if a == b and a == c:
        return "equilátero"
    elif b == c and b != a:
        return "isóceles"
    else:
        return "escaleno"
    
        