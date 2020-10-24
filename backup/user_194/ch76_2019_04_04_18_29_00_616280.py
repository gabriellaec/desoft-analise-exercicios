def aniversariantes_de_setembro(d):
    c = {}
    for nomes,datas in d.items():
        if '/09/' in datas:
            c[nomes] = datas
    return c
    