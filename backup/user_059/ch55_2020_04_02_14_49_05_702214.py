def encontra_maximo(lista):
    lx = []
    ly = []
    lz = []
    lx.append(lista[0])  
    lx.append(lista[1]) 
    lx.append(lista[2]) 
    noval = [0]*3
    noval[0] = max(x)
    noval[1] = max(y)
    noval[2] = max(z)
    j = max(noval)
    return j
