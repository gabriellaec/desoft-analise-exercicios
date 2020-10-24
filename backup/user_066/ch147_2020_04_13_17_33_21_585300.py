def mais_frequente(lista):
    def conta_ocorrencias(lista):
    dicionario={}
    for i in lista:
        if i in dicionario:
            dicionario[i]+=1
        else:
            dicionario[i]=1
    return dicionario
    dicionario = conta_ocorrencias(lista)
    k = 0
    maior_ocorrencia=0
    for i,j in dicionario.itens():
        if j >k:
            k=j
            maior_ocorrencia = i
    return i