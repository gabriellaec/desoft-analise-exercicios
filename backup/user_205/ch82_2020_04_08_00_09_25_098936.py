def primeiras_ocorrencias(x):
    dic = {}
    for caractere in x:
        dic[caractere]=x.find(caractere)
    return dic