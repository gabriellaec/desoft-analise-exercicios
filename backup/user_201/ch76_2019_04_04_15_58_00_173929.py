def aniversariantes_de_setembro(anivs):
    niver_set={}
    for e,data in anivs.items():
        mes=data[4:6]
        if mes == '09':
            niver_set[e]=data
    return niver_set