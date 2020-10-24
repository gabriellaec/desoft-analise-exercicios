def primeiras_ocorrencias(texto):
    dic = {}
    cont = 0
    for let in texto:
        if let not in dic:
            dic[let] = cont
        cont += 1
    return dic