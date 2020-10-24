def encontra_maximo(matriz):
    matriz=[[1,2,3],[4,5,6],[7,8,9]]
    soma=0
    maior=lista[0] 
    i=0
    for val in matriz[i]:
        soma+=val
        if val>maior:
        maior=val
        i+=1
    return matriz
        