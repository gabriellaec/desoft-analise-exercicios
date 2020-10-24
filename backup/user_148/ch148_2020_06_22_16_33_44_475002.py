def conta_letras(palavra):
    dic = {}
    for l in palavras:
        dic[l] = palavra.count(l)
        
    return dic
