def classifica_triangulo(x,y,z):
    if x == y:
        if y == z and x == z: 
            return "equilátero"
        else: 
            return "isósceles"
    elif x == z:
        return "isósceles"
    elif y == z:
        return "isósceles"
    else:
        return "escaleno"
    
print(classifica_triangulo(1,1,2))