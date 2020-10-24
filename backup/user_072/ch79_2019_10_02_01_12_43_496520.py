def  monta_dicionario(lista1,lista2):
    dic={}
    i=0
    while i<len(lista1):
        dic[lista1[i]]=lista2[i]
        i+=1
    return dic
        
        