def classifica_triangulo(x,y,z):
    if x==y!=z:
        return ('isoceles')
    elif x==y==z:
        return ('Equilatero')
    else:
        return ('Escaleno')