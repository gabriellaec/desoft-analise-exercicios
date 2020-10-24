def conta_bigramas(texto):
    cont={}
    for bi in texto:
        if not bi in cont:
            cont[letra]=1
        else:
            contagem[letra]+=1
    return cont
