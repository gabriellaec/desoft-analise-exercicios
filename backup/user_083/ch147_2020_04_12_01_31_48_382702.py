def mais_frequente(lista):
    dicionario={}
    a=0
    for i in (lista):
        if i in dicionario:
            dicionario[i]+=1
        else:
            dicionario[i]=1
    palavra= ''
    for c in dicionario.keys():
        if dicionario[c]>a:
            dicionario[c]=a
            palavra=a
    return palavra