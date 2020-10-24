def aniversariantes_de_setembro(dicionario):
    novo_dicio=dict()
    for c,v in dicionario.items():
        if v[3]=="0" and v[4]=="9":
            novo_dicio[c]=v
    return novo_dicio
    