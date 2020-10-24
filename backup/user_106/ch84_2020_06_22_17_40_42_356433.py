def inverte_dicionario(nomida):
    idanom = {}
    for i in nomida:
        idanom[nomida[i]].append(i)
    return idanom