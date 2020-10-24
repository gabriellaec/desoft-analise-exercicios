def aniversariantes_de_setembro(dic):
    niver_set={}
    for i in range(len(dic)):
        if dic[i][0][3:5] == '09':
            niver_set[dic[i]]= dic[i][0]
    return niver_set