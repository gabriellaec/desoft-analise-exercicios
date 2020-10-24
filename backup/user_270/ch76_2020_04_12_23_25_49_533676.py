def aniversariantes_de_setembro(d):
    new_d = {}
    for k,v in d.items():
        if k[2] == "0" and k[3] == "9" :
            new_d[k] = v
    return new_d