def aniversariantes_de_setembro(dic):
    set={}
    for k,v in dic.items():
        if v[5] == 9:
            set[k]=v
    return set        