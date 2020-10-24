def aniversariantes_de_setembro(dic):
    niver = dict()
    for i in dic:
        if '/09/' in dic[i]:
            niver[i] = dic[i] 
    return niver