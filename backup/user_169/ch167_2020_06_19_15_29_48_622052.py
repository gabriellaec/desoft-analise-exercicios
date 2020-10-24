def bairro_mais_custoso(dicionario):
    
    dicionario2={}
    
    for i in dicionario:
        dicionario2[i]=0
        for e in dicionario[i][6:]:
            dicionario2[i]+=e

    

    return max(dicionario2)
