def monta_dicionario(lista1, lista2):
    dicionario={}
    indice=0
    for i in lista1:
        dicionario[i]=lista2[indice]
        indice+=1
    
    return dicionario