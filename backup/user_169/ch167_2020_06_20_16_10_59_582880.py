def bairro_mais_custoso(dicionario):
    
    dicionario2={}
    lista=[]
    maior=0
    dicionario3={}
    for i in dicionario:
        dicionario2[i]=0
        for e in dicionario[i][6:]:
            dicionario2[i]+=e

    for k,v in dicionario2.items():
        lista.append(v)
        dicionario3[v]=k
    

    for e in lista:
        if e>maior:
            maior=e
            

    for i in dicionario3:
        if maior==i:
            return dicionario3[maior]