def conta_ocorrencias (l1):
    dicionario = {}
    
    for i in l1:
        if i not in dicionario:
            dicionario[i]=1
            

        else:
            dicionario[i] = dicionario[i]+1
        
    return dicionario


def mais_frequente(l1):
    dicionario = conta_ocorrencias(l1)
    a = 0

    for i in dicionario:
        if dicionario[i]>a:
            nome = i
            a = dicionario[i]

    return nome