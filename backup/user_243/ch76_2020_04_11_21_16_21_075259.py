def aniversariantes_de_setembro(dic):
    dic2={}
    for i,t in dic.items():
        if i[3]==0 and i[4]==8:
            dic2[t]=i
        else:
            dic2={}
    return dic2
        