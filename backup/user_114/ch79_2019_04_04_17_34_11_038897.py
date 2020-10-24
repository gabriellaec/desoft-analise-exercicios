def monta_dicionario(lista1,lista2):
    dict={}
    if len(lista1)==len(lista2):
        for i in range(0,len(lista1)):
            dict[lista1[i]]=lista2[i]
            return dict