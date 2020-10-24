def aniversariantes_de_setembro(dic):
    novo = {}
    for i in dic:
        if i.values[3] == 0:
            if dic.values[4] == 9:
                novo[i] = i.values
            else:
                i = i
        else:
            i = i
    return novo
                
                
    