def aniversariantes_de_setembro(dic1):
    dic2={}
    i=0
    for nome in dic1:
        if dic1[nome][3:4]=='09':
            dic2[i]=dic1[nome]
            i+=1
    return dic2