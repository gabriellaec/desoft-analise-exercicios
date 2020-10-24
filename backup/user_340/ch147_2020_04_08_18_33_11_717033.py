def mais_frequente(lista):
    dicionario={}
    for t in lista:
        if t in dicionario:
            dicionario[t]+=1
        else:
            dicionario[t]=1
    maior=0
    palavra=''
    for i, t in dicionario.items():
        if t>maior:
            maior=t
            palavra=i
    return palavra
        
        