def aniversariantes_de_setembro(dic):
    niver_set={}
    for nome,data in dic.items():
        if data[3:5] == '09':
            niver_set[nome]=data
    return niver_set