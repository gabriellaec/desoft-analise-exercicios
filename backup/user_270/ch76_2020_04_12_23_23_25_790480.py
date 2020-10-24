def aniversariantes_de_setembro(d):
    new_d = {}
    for k,v in d.items():
        if k[3] == "0" and k[4] == "9" :
            new_d[k] = v
    return new_d