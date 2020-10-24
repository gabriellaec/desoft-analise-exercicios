def aniversariantes_de_setembro(dic):
    dicionario ={}
    for p,n in dic.items():
        if n[3] == "0" and n[4] == "9":
            dicionario[p] = n
    return dicionario