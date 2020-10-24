def monta_dicionario(lista1, lista2):
    dicionario={}
    elementoslista2=[]
    n=0
    for i in lista2:
        elementoslista2.append(i)
    for i in lista1:
        dicionario[i]=elementoslista2[n]
        n+=1
    return dicionario
        