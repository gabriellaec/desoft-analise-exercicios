def conta_ocorrencias(lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    return dicionario

def mais_frequente(dicionario):
    for i in dicionario.keys:
        a = i
        if i > a:
            palavra = a
    return a