def aniversariantes_de_setembro(datas):
    setem = dict()
    for n, d in datas.items():
        if d[3:5] == '11':
            setem[n] = d
    return setem  