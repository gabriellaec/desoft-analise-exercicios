def classifica_triangulo(x,y,z):
    if x == y and x == z:
        return "equilátero"
    if x == y and x != z: 
        return "isósceles"
    if x != y and x == z: 
        return "isósceles"
    if y == z and y != x: 
        return "isósceles"
    else:
        return "escaleno"