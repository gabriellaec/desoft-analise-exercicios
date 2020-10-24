def aniversariantes_de_setembro(d1):
    d2 = {}
    for k,v in d1.items():
        if v[4] == "9":
            d2[k] = v
    return d2