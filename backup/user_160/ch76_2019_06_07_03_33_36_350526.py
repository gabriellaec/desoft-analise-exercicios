def aniversariantes_de_setembro(n):
    dicionario2 = {}
    for k,v in n.items():
        if v[4] == "9":
            dicionario2[k] = v
    return dicionario2