def encontra_maximo(matriz):
    maxi=0
    for i in matriz:
        for e in i:
            if e>maxi:
                maxi=e
    return maxi
            