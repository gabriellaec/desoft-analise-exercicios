def aniversariantes_de_setembro(dic):
    dic2 = {}
    for i in dic:
        if dic [i][3:5] == '09':
            dic2[i] = dic[i]
            
    return dic2