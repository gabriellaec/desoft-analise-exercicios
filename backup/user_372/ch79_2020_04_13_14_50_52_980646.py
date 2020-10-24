def monta_dicionario(lista1,lista2):
    len(lista1)==len(lista2)
    i=0
    dic={}
    while i<len(lista1) and i<len(lista2):
        dic[lista1[i]]=lista2[i]
        i=i+1
    return dic
    
    
        