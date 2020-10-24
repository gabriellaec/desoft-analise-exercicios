def bairro_mais_custoso(dicionario):
    
    dicionario2={}
    lista=[]
    dicionario3={}
    for i in dicionario:
        dicionario2[i]=0
        for e in dicionario[i][6:]:
            dicionario2[i]+=e

    for k in dicionario2:
        lista.append(dicionario2[k])
        dicionario3[dicionario2[k]]=k
        for e in lista:
            if e == dicionario3[dicionario2[k]]:
                return k

        
    return k
    