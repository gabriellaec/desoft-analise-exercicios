def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return ('equilátero')
    elif x==y and x!=z:
        return ('isóceles')
    elif  z==y and z!=x:
        return ('isóceles')
    else:
        return ('escaleno')