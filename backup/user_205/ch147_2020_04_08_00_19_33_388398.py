def conta_ocorrencias(lista): 
    dic={}
    for palavras in lista:
        dic[palavras]=lista.count(palavras)
    return dic
def mais_frequente(lista2):
    dic = conta_ocorrencias(lista2)
    for nome in dic.keys():
        for numeros in dic.values():
            return dic[nome]=max(dic[numero])
            