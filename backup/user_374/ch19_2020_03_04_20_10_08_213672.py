
def classifica_triangulo(x,y,z):
    if (x==y and y==z and x==z):
        return "equilátero"
    elif x!=y and x!=z and y!=z:
        return "escaleno"
    else:
       return "isósceles"
print(classifica_triangulo(1,1,2))
    
