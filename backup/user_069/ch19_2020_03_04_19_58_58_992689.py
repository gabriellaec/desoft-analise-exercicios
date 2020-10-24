def classifica_triangulo (x,y,z):
    if x==y and x==z and y==z:
        return "equilátero"
    if x!=y and x!=z and y!=z:
        return "escaleno"
    else:
        return "isóceles"
