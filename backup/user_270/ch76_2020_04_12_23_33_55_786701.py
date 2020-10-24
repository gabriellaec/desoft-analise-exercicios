def aniversariantes_de_setembro(d):
    new_d = {}
    for k,v in d.items():
        if v[3] == "0" and v[4] == "9" :
            new_d[k] = v
    return new_d