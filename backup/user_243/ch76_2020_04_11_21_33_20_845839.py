def aniversariantes_de_setembro(dic):
    dic2={}
    for i,t in dic.items():
        if t[4]=="9":
            dic2[i]=t
    return dic2
        