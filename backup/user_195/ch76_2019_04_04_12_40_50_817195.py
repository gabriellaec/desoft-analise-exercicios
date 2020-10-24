def aniversariantes_de_setembro(D):
    C={}
    for nomes,aniversarios in D.items():
        if "/09/" in aniversarios:
            C[nomes]=aniversarios
    return C