def acha_bigramas(palavra):
    i=0
    dicionario={}
    while i < len(palavra)-1:
        v=palavra[i]+palavra[i+1]
        if v not in dicionario:
            dicionario[v]=1
        elif v in dicionario:
            dicionario[v]+=1
        i+=1
    return dicionario
b='banana nanica'
print(acha_bigramas(b))
