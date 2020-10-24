def monta_dicionario(x):
    lista1=['a','b','c','d']
    lista2=[1,2,3,4]
    dicionario={}
    for i in range(len(lista1)):
        dicionario[lista1[i]] =lista2[i]
    return dicionario