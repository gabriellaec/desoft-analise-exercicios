def conta_ocorrencias (lista_palavras):
    dicio = {}
    for word in lista_palavras:
        if word in dicio:
            dicio[word] +=1
        else:
            dicio[word] =1
    return dicio



def mais_frequente(conta_ocorrencias):
    max = 0
    for v in dicio.values():
        if max < v:
            max = v
    for k, v in dicio.items():
        if v == max:
            chave = k
            print (chave)
    return chave