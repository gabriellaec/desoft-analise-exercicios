def inverte_dicionario(dicionario):
    inv_dicionario = {}
    for k, v in dicionario.items():
        if v in inv_dicionario:
            inv_dicionario[v].append(k)
        else:
            inv_dicionario = [k]
    return inv_dicionario
   