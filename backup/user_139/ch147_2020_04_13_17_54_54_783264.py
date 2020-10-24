def conta_ocorrencias (lista):
    dic = {}
    for palavra in lista:
        if not palavra in dic:
            dic [palavra] = 1
        else:
            dic [palavra] += 1
    return dic
def mais_frequente (dic):
    palavra = ''
    for e in dic.values:
        if e > 0:
            palavra.append 
        