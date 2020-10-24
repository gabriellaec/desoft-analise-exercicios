def  encontra_maximo(matriz):
    lista_matriz=[]
    for ele in matriz:
        for elementos_de_elementos in ele:
            lista_matriz.append(elementos_de_elementos)
    nmax=max(lista_matriz)
    return nmax