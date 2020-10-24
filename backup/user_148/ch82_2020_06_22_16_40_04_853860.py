def primeiras_ocorrencias(palavra):
    dic = {}
    for l in palavra:
        dic[l] = palavra.find(l)
        
    return dic
