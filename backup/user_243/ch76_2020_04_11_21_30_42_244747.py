def aniversariantes_de_setembro(dic):
    dic2={}
    for i,t in dic.items():
        if i[4]=="9":
            dic2[t]=i
    return dic2
        