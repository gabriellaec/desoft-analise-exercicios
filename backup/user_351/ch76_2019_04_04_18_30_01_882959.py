def aniversariantes_de_setembro(dicionario):
    c ={}
    for nomes,datas in dicionario.items():
        if "/09/" in datas:
            c[nomes]=datas
    return c