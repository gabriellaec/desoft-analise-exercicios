def mais_populoso(dicionario):
    lista=[]
    lista2=[]
    for i in dicionario:
        lista.append(dicionario[i])
    
    for e in lista:
        for k,v in e.items():
            lista2.append(v)

    
    return max(lista2)
    