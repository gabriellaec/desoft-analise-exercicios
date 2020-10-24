def conta_letras(palavra):
    dic = {}
    for l in palavra:
        dic[l] = palavra.count(l)
        
    return dic
