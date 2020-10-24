def conta_ocorrencias(lista):
    dicionario={}
    for i in lista:
        if i not in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
    return dicionario

listaB=[]

print=(conta_ocorrencias(listaB))