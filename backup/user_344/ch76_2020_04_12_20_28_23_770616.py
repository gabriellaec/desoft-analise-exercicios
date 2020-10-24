def  aniversariantes_de_setembro(dic):
    DIC2 = {}
    for i in dic:
        if dic[i][3:5] == '09':
            DIC2[i] = dic[i]
    return DIC2