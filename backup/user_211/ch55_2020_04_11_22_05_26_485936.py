def encontra_maximo(matriz):
    lista=[]
    lista2=[]
    for i in range(0,3):
        for j in range(0,3):
            lista.append(matriz[i][j])
    for i in range(0,len(lista)):
        lista2.append(abs(lista[i]))
        
    return max(lista2)