def primeiras_ocorrencias(string):
    dic={}
    for letra in string:
        if letra not in dic:
            dic[letra]= 1
        else:
            dic[letra] += 1
     return dic
