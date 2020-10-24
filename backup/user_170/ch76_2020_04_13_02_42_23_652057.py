def aniversariantes_de_setembro(aniversarios):
    setembro = {}
    for n, v in aniversarios.items():
        if v[4] ==  9:
            setembro[n] = v
    return setembro