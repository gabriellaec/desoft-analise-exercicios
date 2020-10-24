def encontra_maximo(lista):
    lx = []
    ly = []
    lz = []
    lx.append(lista[0])  
    lx.append(lista[1]) 
    lx.append(lista[2]) 
    noval = [0]*3
    noval[0] = max(lx)
    noval[1] = max(ly)
    noval[2] = max(lz)
    j = max(noval)
    return j
