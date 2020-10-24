def conta_ocorrencias(l):
    dicionario = {}
    for i in range(len(l)):
        if l[i] not in dicionario:
            dicionario[l[i]] = l.count(l[i])
            
    return dicionario

def mais_frequente(l):
    dicionario = conta_ocorrencias(l)
    resultado = ["", 0]
    for x in dicionario:
        if dicionario[x] > resultado[1]:
            resultado = [x, dicionario[x]]
            
    return resultado[0]