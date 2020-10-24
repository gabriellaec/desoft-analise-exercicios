def aniversariates_de_setembro(x):
    ste = {}
    for i,e in x.items():
        if "/09/" in e:
            ste[i] = e
    return ste