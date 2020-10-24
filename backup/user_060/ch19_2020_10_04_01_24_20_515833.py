def lados(x, y, z):
    if x!=y!=z:
        return "escaleno"
    elif x=y=z:
        return "equilátero"
    else:
        return "isósceles"