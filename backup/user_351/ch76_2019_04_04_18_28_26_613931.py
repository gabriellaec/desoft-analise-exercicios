def aniversariantes_de_setembro(dicionario):
    c ={}
    for nomes,datas in dicionario.itens():
        if "/09/" in datas:
            c[nomes]=datas