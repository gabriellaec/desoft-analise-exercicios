def monta_dicionario(lista1,lista2):
    dic={}
    lista3=[]
    i=0
    while i<len(lista1):
        lista3.append([lista1[i],lista2[i]])
        i+=1
    for k in range(0,len(lista3)):
        dic[lista3[k][0]]=lista3[k][1]
    return dic