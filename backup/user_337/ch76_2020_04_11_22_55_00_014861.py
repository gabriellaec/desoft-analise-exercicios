def aniversariantes_de_setembro(dic):
    set = {}
    valores = dic.values()
    chaves = dic.keys()
    for i in valores:
        if i[5] == 9:
            for k in dic:
                if dic[k] == i:
                    set[k] = i
            
            