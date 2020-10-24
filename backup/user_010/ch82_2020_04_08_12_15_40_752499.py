def primeiras_ocorrencias (str):
    dic={}
    for i,letra in enumerate(str):
        if letra not in dic:
            dic [letra]=i
    return dic